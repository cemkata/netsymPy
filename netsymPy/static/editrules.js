function checkboxHandler(){
	checkboxes = document.getElementsByTagName("input"); // The first 3 inputs are the select all and the two hiden fields for the POST of the form

	for (var i = 3; i < checkboxes.length; i++) {
		var checkbox = checkboxes[i];
		checkbox.onclick = function() {
			checkbocChecked();
			//x = x.getElementsByTagName("img")[0];
			if (this.checked){
				formArray.push(this.id);
				this.parentNode.parentNode.className ='selected';

			}else{
				for(var i = formArray.length - 1; i >= 0; i--) {
					if(formArray[i] === this.id) {
						formArray.splice(i, 1);
					}
				}
				this.parentNode.parentNode.className ='';
			}
		};
	}
}



function selectAll(){
  var source = document.getElementsByName('deletAll')[0];
  var checkboxes = document.getElementsByName('selectedCheckbox');
  for(var i=0; i<checkboxes.length; i++) {
    checkboxes[i].checked = source.checked;
    formArray.push(checkboxes[i].id);
  }

  if(source.checked){
        document.getElementsByName("btnDel")[0].disabled = false;
        document.getElementsByName("btnStop")[0].disabled = false;
  }else{
        document.getElementsByName("btnDel")[0].disabled = true;
        document.getElementsByName("btnStop")[0].disabled = true;
  }

}

function checkbocChecked(){
  var checkboxes = document.getElementsByName('selectedCheckbox');
  var n = 0;
  for(var i=0; i<checkboxes.length; i++) {
    if (checkboxes[i].checked) n++;
  }
  if(n == 1){
	document.getElementsByName("btnEdit")[0].disabled = false;
	document.getElementsByName("btnCopy")[0].disabled = false;
	document.getElementsByName("btnCopyDifIPVer")[0].disabled = false;
  }else{
	document.getElementsByName("btnEdit")[0].disabled = true;
	document.getElementsByName("btnCopy")[0].disabled = true;
	document.getElementsByName("btnCopyDifIPVer")[0].disabled = true;
  }
  if(n != 0){
  	document.getElementsByName("btnDel")[0].disabled = false;
	document.getElementsByName("btnStop")[0].disabled = false;
  }else{
  	document.getElementsByName("btnDel")[0].disabled = true;
	document.getElementsByName("btnStop")[0].disabled = true;
  }
}

function addRowHandlers() {
	var table = document.getElementById("rules");
	var frstRow = table.getElementsByTagName("tr")[0];
	for (var i = 1; i < frstRow.cells.length; i++) {
		var currentCell = frstRow.cells[i];
		var createClickHandler =
			function(tableCell)
			{
				return function() {
								selecteCell = tableCell.cellIndex;
                                                                if (document.getElementById("rmenu").className != "show"){
									document.getElementById("rmenu").className = "show";
									document.getElementById("rmenu").style.top = mouseY(event) + 'px';
									document.getElementById("rmenu").style.left = mouseX(event) + 'px';
								}else{
									hidemenu();

								}
						 };
			};
		frstRow.cells[i].onclick = createClickHandler(currentCell);
	}
}

function showAll() {
	var table = document.getElementById("rules");
	var frstRow = table.getElementsByTagName("tr")[0];
	for (i = 1; i < frstRow.cells.length; i++) {
		show_hide_column(i, true);
		}
}
function show_hide_column(col_no, do_show) {
	var stl;
	if (do_show){
		stl = ''
	}else{
		stl = 'none';
	}
	var tbl = document.getElementById("rules");
	var rows = tbl.getElementsByTagName('tr');
	if(col_no == 25){
		var cels = rows[0].getElementsByTagName('td')
		cels[col_no].style.display=stl;
        for (var row=1; row<rows.length;row++) {
            cels = rows[row].getElementsByTagName('td')
            cels[col_no].style.display=stl;
			cels[col_no + 1].style.display=stl;
        }
	}else{
         for (var row=0; row<rows.length;row++) {
             var cels = rows[row].getElementsByTagName('td')
             cels[col_no].style.display=stl;
         }
	}


}

function sortTable(id, AZ) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("rules");
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
	//start by saying: no switching is done:
	switching = false;
	rows = table.getElementsByTagName("TR");
	/*Loop through all table rows (except the
	first, which contains table headers):*/
	for (i = 1; i < (rows.length - 1); i++) {
	  //start by saying there should be no switching:
	  shouldSwitch = false;
	  /*Get the two elements you want to compare,
	  one from current row and one from the next:*/
	  x = rows[i].getElementsByTagName("TD")[id];
	  y = rows[i + 1].getElementsByTagName("TD")[id];
	  //check if the two rows should switch place:
	  if(id == 1 ){
	  	  x = x.getElementsByTagName("img")[0];
	  	  y = y.getElementsByTagName("img")[0];
		  if(AZ){
			  if (x.id.toLowerCase() > y.id.toLowerCase()) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }else{
			  if (x.id.toLowerCase() < y.id.toLowerCase()) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }
	  }else if(id == 2 || id == 5){
		  if(AZ){
			  if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }else{
			  if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }
	  }else{
		  if(AZ){
			  if (parseInt(x.innerHTML) > parseInt(y.innerHTML)) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }else{
			  if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			  }
		  }
	  }

	}
		if (shouldSwitch) {
		  /*If a switch has been marked, make the switch
		  and mark that a switch has been done:*/
		  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
		  switching = true;
		}
	  }
}

function hidemenu(){
	document.getElementById('rmenu').className = 'hide';
}

function mouseX(evt) {
	if (evt.pageX) {
		return evt.pageX;
	} else if (evt.clientX) {
	   return evt.clientX + (document.documentElement.scrollLeft ?
		   document.documentElement.scrollLeft :
		   document.body.scrollLeft);
	} else {
		return null;
	}
}
function mouseY(evt) {
	if (evt.pageY) {
		return evt.pageY;
	} else if (evt.clientY) {
	   return evt.clientY + (document.documentElement.scrollTop ?
	   document.documentElement.scrollTop :
	   document.body.scrollTop);
	} else {
		return null;
	}
}
