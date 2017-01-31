function validateUserDelete() {
	alert("clicky");
}

function validateUserForm() {
	var title = $("#title").val();
	var initials = $("#initials").val();
	var name = $("#name").val();
	var surname = $("#surname").val();
	var email = $("#email").val();
	var cell = $("#cell").val();
	var userId = $("#userId").val();
	var status = $("#status").val();

	if (title == null || title == "")
	{
		// $("#title").addClass
	}

    if (title == null || title == "" ||
		initials == null || initials == "" ||
		name == null || name == "" ||
		surname == null || surname == "" ||
		email == null || email == "" ||
		cell == null || cell == "" ||
		userId == null || userId == "" ||
		status == null || status == "") {
        alert("Please fill in all fields");
        return false;
    }

	if (password != passwordConfirm){
		alert("Passwords do not correspond");
		return false;
	}

	if (status != 'A' && status != 'a' && status != 'U' && status != 'u')
	{
		alert("Please select a valid status");
		return false;
	}
	
	if (userId.length < 8 || userId.length > 8)
	{
		alert("Invalid user ID length");
		return false;
	}

	for (i = 0; i < userId.length; ++i)
	{
		if (isNaN(userId[i]))
		{
			alert("Please enter a valid user ID");
			return false;
		}
	}
	
	if (cell.length < 10 || cell.length > 10)
	{
		alert("Invalid cell number length");
		return false;
	}	

	for (i = 0; i < cell.length; ++i)
	{
		if (isNaN(cell[i]))
		{
			alert("Please enter a valid cell number");
			return false;
		}
	}
}


/* Nigel
	Delete Confirmation function for form submission
*/
function confirmDeletion() {
	return confirm('Are you sure you wish to delete this?');
}

function confirmSubmit() {
	return confirm('Are you sure you wish to submit this?');
}
