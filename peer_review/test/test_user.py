from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from peer_review.models import User

from peer_review.views import *
import json

#
#from django.test.utils import setup_test_environment
#setup_test_environment()
#


class UserTests(TestCase):
    def test_test(self):
        """
        2 + 2 should equal 4
        """
        ans = 2 + 2
        self.assertEqual(ans, 4)

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bob@bob.com', 'bob', 'bob', userId=str(1234), surname="bob", initials="B")
        self.user = User.objects.create_user('joe@joe.com', 'joe', 'joe', userId=str(5678), surname="Joe", initials="J")
        User.objects.create_superuser('admin@admin.com', 'admin', userId=str(1111))
        #self.user2 = User.objects.create_user('joe@joe.com', 'joe')

    # Simple test to see if questionAdmin is rendered
    def test_questionAdmin(self):
        self.client.login(username='1111', password='admin')
        url = reverse('questionAdmin')
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/questionAdmin.html')

    # Simple test to see if questionnaireAdmin is rendered
    def test_questionnaireAdmin(self):
        self.client.login(username='1234', password='bob')
        url = reverse('questionnaireAdmin')
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/questionnaireAdmin.html')

    # Simple test to see if userdAdmin is rendered
    def test_user_list(self):
        print("--- user_list Test ---\n")
        self.client.login(username='1234', password='bob')
        url = reverse('userAdmin')
        response = self.client.get(url, follow = True)
        print(response.context['users']())
        self.assertIn(self.user, response.context['users']())

    # Simple test to see if accountDetails is rendered
    def test_account_details(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = '/accountDetails/1234'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/accountDetails.html')

    # Simple test to see if login is rendered
    def test_login(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/login.html')

    # Simple test to see if maintainRound is rendered
    def test_maintain_round(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('maintainRound')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/maintainRound.html')

    # Simple test to see if activeRounds is rendered
    def test_active_rounds(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = 'activeRounds/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/activeRounds.html')

    # Simple test to see if maintainTeam is rendered
    def test_maintain_team(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = 'maintainTeam'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/maintainTeam.html')

        print("\n--- END ---\n")

    # Unit Test
    def test_get_user(self):
        # Tests if current user is recognised
        print("--- get_user Test ---\n")
        self.client.login(username='5678', password='joe')
        response = self.client.get('/accountDetails/1234')
        request = response.wsgi_request
        logged_user = json.loads(get_user(request, request.user.userId).content.decode())
        expected_user = json.loads(get_user(request, "5678").content.decode()) # Joe userId
        print("Logged user: " + str(logged_user))
        print("Expected user: " + str(expected_user))
        self.assertEqual(logged_user, expected_user)
        print("\n--- END ---\n")

    def test_authentication(self):
        # Test redirection when access is granted and denied
        print("--- Authenticatoin Test ---\n")
        self.client.login(username='5678', password='joe')
        response = self.client.get('/accountDetails/')
        request = response.wsgi_request
        print("Granted Status Code: " + str(response.status_code))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/accountDetails.html')
        # Logout and try false details
        self.client.logout()
        self.client.login(username='1234', password='bobby')
        response = self.client.get('/accountDetails/')
        request = response.wsgi_request
        print("Denied Status Code: " + str(response.status_code))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'peer_review/userError.html')
        print("\n--- END ---\n")
