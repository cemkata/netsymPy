function checkDeletion(){
	var answer = confirm("Delete all rules (The whole database)?")
	if (answer) {
	    document.getElementsByName("exsecutionAction")[0].value='ClearRules';
	    document.getElementById("actionForm").submit();
	}
	else {
	    return;
	}
}

function checkJS(){
	var hiddenDiv = document.getElementsByName("jsEnabled")[0];
	var visibleDiv = document.getElementsByName("jsDisabled")[0];
	hiddenDiv.style.display = 'block';
	visibleDiv.style.display = 'none';
}

function setActionHome(name){
	switch(name){
		case 'AddV4': document.getElementsByName("exsecutionAction")[0].value='AddV4'; break;
		case 'AddV6': document.getElementsByName("exsecutionAction")[0].value='AddV6'; break;
		case 'StartTC': document.getElementsByName("exsecutionAction")[0].value='StartTC'; break;
		case 'StopTC': document.getElementsByName("exsecutionAction")[0].value='StopTC'; break;
		case 'ClearRules': checkDeletion(); return;
		case 'EditRules': document.getElementsByName("exsecutionAction")[0].value='EditRules'; break;
		case 'Statistic': document.getElementsByName("exsecutionAction")[0].value='Statistic'; break;
		case 'Help': document.getElementsByName("exsecutionAction")[0].value='Help'; break;
		case 'Index': document.getElementsByName("exsecutionAction")[0].value='Index'; break;
	}
	document.getElementById("actionForm").submit();
	return true;
}

function setActionEdit(name){
	switch(name){
		case 'delete':
						var temp='';
						for(var i=0; i<formArray.length; i++){
							temp+=formArray[i];
							temp+=";"
						}
						document.getElementsByName("editFormAction")[0].value='delete';
						document.getElementsByName("ruleID")[0].value=temp;
						var answer = confirm("Are you sure?")
						if (answer) {
						    break;
						}else {
						    return;
						}

		case 'edit':
						document.getElementsByName("editFormAction")[0].value='edit';
						document.getElementsByName("ruleID")[0].value=formArray[0];
						break;

		case 'disable':
						var temp='';
						for(var i=0; i<formArray.length; i++){
							temp+=formArray[i];
							temp+=";"
						}
						document.getElementsByName("editFormAction")[0].value='disable';
						document.getElementsByName("ruleID")[0].value=temp;
						break;

		case 'copy':
						document.getElementsByName("editFormAction")[0].value='copy';
						document.getElementsByName("ruleID")[0].value=formArray[0];
						break;

		case 'changeIp':
						document.getElementsByName("editFormAction")[0].value='changeIp';
						document.getElementsByName("ruleID")[0].value=formArray[0];
						break;
	}
	document.getElementById("actionForm").submit();
	return true;
}
