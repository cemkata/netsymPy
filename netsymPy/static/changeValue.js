function validateForm(){
	var errorCount = document.getElementById("error");
	if(!errorCount)
	{
		//alert("No errors");
		return true;
	}else{
		//alert("Error!");
		return false;
	}
}

function changeValue(name ,optId){
    //alert(name);
	switch(optId){
		case 0: document.getElementsByName(name)[0].value='0';
				document.getElementsByName(name)[0].disabled = true;
				break;
		case 1: document.getElementsByName(name)[0].value='17';
				document.getElementsByName(name)[0].disabled = true;
				break;
		case 2: document.getElementsByName(name)[0].value='6';
				document.getElementsByName(name)[0].disabled = true;
				break;
		default: document.getElementsByName(name)[0].value='100';
				document.getElementsByName(name)[0].disabled = false;
				break;
	}
}

function testFloat(name){
	var testValue = document.getElementsByName(name)[0];
	var floatValue = testValue.value.replace(",", ".");
	
	var count = (floatValue.match(/\.\\./g) || []).length;
	if(count > 0){
			testValue.setAttribute("id", "error");
			return;
		}
	count = (floatValue.match(/\./g) || []).length;
	if(count > 1){
			testValue.setAttribute("id", "error");
			return;
		}
		
	var floatDigits = floatValue.split(".");
	for(var i=0; i<floatDigits.length; i++){
		var isnum = /^\d+$/.test(floatDigits[i]);
		if(!isnum){
			testValue.setAttribute("id", "error");
			return;
		}
	}
	testValue.removeAttribute("id");
}

function testDigit(name){
	var testValue = document.getElementsByName(name)[0];
	/*if(testValue.value == ""){
			alert("NULL");
			testValue.setAttribute("id", "error");
			return;
	}*/
	var isnum = /^\d+$/.test(testValue.value);
	if(isnum){
		testValue.removeAttribute("id");
		return;
	}else{
		testValue.setAttribute("id", "error");
		return;
	}
}

function checkipV4(name){
	var testValue = document.getElementsByName(name)[0];
	/*if(testValue.value == ""){
			alert("NULL");
			testValue.setAttribute("id", "error");
			return;
	}*/
	if(testValue.value.toLowerCase() == "any"){
		testValue.removeAttribute("id");
		return;
	}	
	var ip = testValue.value.split(".");
	if(ip.length == 4){
		for (var i=0; i<ip.length; i++){
			var isnum = /^\d+$/.test(ip[i]);
			if(!isnum){
				testValue.setAttribute("id", "error");
				return;
			}else{
				var octet = parseInt(ip[i]);
				if(octet>255 || octet < 0){
					testValue.setAttribute("id", "error");
					return;
				}
			}
		}
		
		testValue.removeAttribute("id");
		return;
	}else{
		testValue.setAttribute("id", "error");
		return;
	}
}

function checkIPv6(name){
	var testValue = document.getElementsByName(name)[0];

	var inputIP = testValue.value;
 	if(inputIP.length > 39){
		testValue.setAttribute("id", "error");
		return;
	}
	
 	if(inputIP.toLowerCase() == "any" || inputIP.toLowerCase() == "0000:0000:0000:0000:0000:0000:0000:0000"){
		testValue.removeAttribute("id");
		return;
	}

		
	var count = (inputIP.match(/:::/g) || []).length;
	if(count > 0){
			testValue.setAttribute("id", "error");
			return;
		}
		
	/*for(var i = 0; i < inputIP.length; i++){
		var count = 0;
		if(inputIP[i] == ":"){
			count++;
			if(count > 2){
				testValue.setAttribute("id", "error");
				return;
			}
		}else{
			count=0;
		}
	}*/
		
	count = (inputIP.match(/::/g) || []).length;
	if(count > 1){
			testValue.setAttribute("id", "error");
			return;
		}


	for(i=0; i<inputIP.length; i++){
		switch(inputIP[i]){
			case '0':
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
			case 'A':
			case 'a':
			case 'B':
			case 'b':
			case 'C':
			case 'c':
			case 'D':
			case 'd':
			case 'E':
			case 'e':
			case 'F':
			case 'f': 
			case ':':break;
			default: 
					testValue.setAttribute("id", "error");
					return;
		}					
	}
	
	//convert the ipV6 to XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
	//var ipv6 = "0000:0000:0000:0000:0000:0000:0000:0000";		
	//var ipv6 = "";
	var ipv6 = ["0", "0", "0", "0", ":", "0", "0", "0", "0", ":","0", "0", "0", "0", ":","0", "0", "0", "0", ":","0", "0", "0", "0", ":","0", "0", "0", "0", ":", "0", "0", "0", "0", ":", "0", "0", "0", "0"];
	
	if(count > 0){
		var ip = inputIP.split("::");
		var additionalZeros = 39 - (inputIP.length-1);
		var uperOctets = ip[0].split(":");
		var lowOctets = ip[1].split(":");
		if(uperOctets!=""){
			for(var i=0; i<uperOctets.length;i++){
				switch(uperOctets[i].length){
					case 1:uperOctets[i]="000"+uperOctets[i]; additionalZeros-=3; break;
					case 2:uperOctets[i]="00"+uperOctets[i]; additionalZeros-=2; break;
					case 3:uperOctets[i]="0"+uperOctets[i]; additionalZeros-=1; break;
					case 4:uperOctets[i]=""+uperOctets[i]; break;
					default: 
							testValue.setAttribute("id", "error");
							return;
				}
			}
		}
		if(lowOctets!=""){
			for(var i=0; i<lowOctets.length;i++){
				switch(lowOctets[i].length){
					case 1:lowOctets[i]="000"+lowOctets[i]; additionalZeros-=3; break;
					case 2:lowOctets[i]="00"+lowOctets[i]; additionalZeros-=2; break;
					case 3:lowOctets[i]="0"+lowOctets[i]; additionalZeros-=1; break;
					case 4:lowOctets[i]=""+lowOctets[i]; break;
					default: 
							testValue.setAttribute("id", "error");
							return;
				}
			}
		}
		var k=0;
		for(var i=0; i<uperOctets.length;i++){
			for(var j=0; j<uperOctets[i].length;j++){
				ipv6[k]=uperOctets[i][j];
				k++;
			}
			k++;
		}
		k+=additionalZeros;
		for(var i=0; i<lowOctets.length;i++){
			for(var j=0; j<lowOctets[i].length;j++){
				ipv6[k]=lowOctets[i][j];
				k++;
			}
			k++;
		}	
	}else{
		var ip = inputIP.split(':');
		
		if(ip.length!=8){
			testValue.setAttribute("id", "error");
			return;
		}
		
		for(var i=0; i<ip.length;i++){
			switch(ip[i].length){
				case 1:ip[i]="000"+ip[i]; break;
				case 2:ip[i]="00"+ip[i]; break;
				case 3:ip[i]="0"+ip[i]; break;
				case 4:ip[i]=""+ip[i]; break;
				default:
						testValue.setAttribute("id", "error");
						return;
			}				
		}
		var k=0;
		for(var i=0; i<ip.length;i++){
			for(var j=0; j<ip[i].length;j++){
				ipv6[k]=ip[i][j];
				k++;
			}
			k++;
		}
	}
	
	testValue.value=ipv6.join("");
	testValue.removeAttribute("id");
}

function checkMAC(name){
	var testValue = document.getElementsByName(name)[0];
	/*if(testValue.value == ""){
			alert("NULL");
			testValue.setAttribute("id", "error");
			return;
	}*/

	if(testValue.value.toLowerCase() == "any"){
		testValue.removeAttribute("id");
		return;
	}
	
	if (testValue.value.length !=17){
		testValue.setAttribute("id", "error");
		return;
	}
	
	var mac = testValue.value.split(":");
	if(mac.length == 6){
		var macAdr="";
		for (var i=0; i<mac.length; i++){
			if(mac[i].length != 2){
				testValue.setAttribute("id", "error");
				return;
			}else{
				macAdr+=mac[i]
			}
		}
	}
	
	for(i=0; i<macAdr.length; i++){
		switch(macAdr[i]){
			case '0':
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
			case 'A':
			case 'a':
			case 'B':
			case 'b':
			case 'C':
			case 'c':
			case 'D':
			case 'd':
			case 'E':
			case 'e':
			case 'F':
			case 'f': break;
			default: 
					testValue.setAttribute("id", "error");
					return;
		}					
	}
	
	testValue.removeAttribute("id");		
}


