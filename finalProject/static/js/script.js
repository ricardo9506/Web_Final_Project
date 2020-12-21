function changeSearchType(){
	var type = document.getElementById("searchtype").value;
	if(type==1){
		document.getElementById("searchingByPrice").style.display='none';
		document.getElementById("searchingByName").style.display='block';
	}else if(type==2){
		document.getElementById("searchingByPrice").style.display='block';
		document.getElementById("searchingByName").style.display='none';
	}
}

function search(type){
	if(type=="name"){
		var key1 = document.getElementById("searchingName").value;
	}else if(type=="price"){
		var key1 = document.getElementById("lowprice").value;
		var key2 = document.getElementById("hightprice").value;
	}else{
		return;
	}
	var xhr = new XMLHttpRequest();
	xhr.open("POST","/search/",true);
	xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	if(type=="name"){
		xhr.send("type="+type+"&key1="+key1);
	}else{
		xhr.send("type="+type+"&key1="+key1+"&key2="+key2);
	}
	xhr.onreadystatechange = function(){
		if(xhr.readyState===4){
			if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
				var res =  eval(xhr.responseText);
				var inner = "<table rules='none'><tr><th>Product Name</th><th>Current Price</th><th>Trading Place</th><th>Phone Number</th><th>Status</th><th>Seller Name</th></tr>";
				if(res.length == undefined){
					inner += "<tr><td colspan='6' style='text-align:center'>No Data</td></tr>"
				}else{
					for(var i = 0;i < res.length;i++){
						inner += "<tr><td><a href='buyer.php?turn=4&id="+res[i][0]+"'>" + res[i][1] + "</a></td><td>" +res[i][2]+"</td><td>"+res[i][3]+"</td><td>"+res[i][4]+"</td><td>"+res[i][5]+"</td><td>"+res[i][6]+"</td></tr>";
					}
				}
				inner += "</table>";
				console.log(inner);
				document.getElementById("searchingReasult").innerHTML=inner;
			}
		}
	}
}

function typecheck(type){
	if(type=='s'){
		document.getElementById("typeB").checked = false;
	}else{
		document.getElementById("typeS").checked = false;
	}
}

function signup(){
	var type;
	var b = document.getElementById("typeB").checked;
	var s = document.getElementById("typeS").checked;
	if(s==true){
		type = "1";
	}else if(b == true){
		type = "2";
	}else{
		alert("Please Choose Type!");
		return;
	}
	
	var id = document.getElementById("id").value;
	var state = document.getElementById("state").innerText;
	var email = document.getElementById("email").value;
	var password = document.getElementById("password").value;
    var spassword = document.getElementById("spassword").value;
    
	if(id==""){
		alert("ID CANNOT BE NULL!");
	}else if(state!="OK!"){
		alert("Check your ID!");
	}else if(password!=spassword){
		alert("Password Not Match!");
	}else{
		var xhr = new XMLHttpRequest();
		xhr.open("POST","/signup/",true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.send("id="+id+"&type="+type+"&email="+email+"&password="+password);
		xhr.onreadystatechange = function(){
			if(xhr.readyState===4){
				if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
					if(xhr.responseText == "1"){
						alert("Sign Up Succeed!\nWelcome to Flea Market");
						window.location.href = "/login/";
					}else{
						alert("Something Wrong!\nPlease Connect to Administrator!");
					}
				}
			}
		}
	}
}

function duplicate(){
	var type;
	var buy = document.getElementById("typeB").checked;
	var sell = document.getElementById("typeS").checked;
	if(sell==true){
		type = "1";
	}else if(buy==true){
		type = "2";
    }else{
        alert("Please Choose Your Account Type!");
        return;
    }
    
    var id = document.getElementById("id").value;
    
	if(id == ""){
		alert("Please input ID!");
	}else{
		var xhr = new XMLHttpRequest();
		xhr.open("POST","/checkId/",true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.send("id="+id+"&type="+type);
		xhr.onreadystatechange = function(){
			if(xhr.readyState===4){
				if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
					console.log(xhr.responseText);
					if(xhr.responseText == "1"){
						var s = document.getElementById("state");
						s.style.color = "green";
						s.innerHTML = "OK!";
					}else{
						var s = document.getElementById("state");
						s.style.color = "red";
						s.innerHTML = "Exists!";
					}
				}
			}
		}
	}
}