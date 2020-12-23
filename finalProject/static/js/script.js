function signout(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/signout/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("abc");
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                window.location.href = "/homepage/"; 
            }else{
                alert("Something Wrong!");
            }
        }
    }
}
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
						inner += "<tr><td><a href='/product/?id="+res[i][0]+"'>" + res[i][1] + "</a></td><td>" +res[i][5]+"</td><td>"+res[i][9]+"</td><td>"+res[i][7]+"</td><td>"+res[i][12]+"</td><td>"+res[i][8]+"</td></tr>";
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

function login(){
	var type;
	var logined;
	var b = document.getElementById("typeB").checked;
	var s = document.getElementById("typeS").checked;
	if(s==true){
		type = "1";
		logined = "/seller/";
	}else if(b == true){
		type = "2";
		logined = "/buyer/";
	}else{
		type = "0";
		logined = "/admin/";
	}
	var id = document.getElementById("id").value;
    var password = document.getElementById("password").value;
    
	if(id==""){
		alert("Please input your ID!")
	}else if(password==""){
		alert("Please input your password!");
	}else{
		var xhr = new XMLHttpRequest();
		xhr.open("POST","/login/",true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.send("id="+id+"&type="+type+"&password="+password);
		xhr.onreadystatechange = function(){
			if(xhr.readyState===4){
				if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
					if(xhr.responseText == "1"){
						window.location.href = logined;
					}else{
						alert("Failed!\nPlease Check your Password or Username!\nOR Connect to Administrator!");
					}
				}
			}
		}
	}
}

function accountChange(item){
    var inner = document.getElementById(item).innerText;
    var changed = prompt("Change",inner);
    if(changed==null||changed==""){
        return;
    }else{
        document.getElementById(item).innerText = changed;
    }
}

function deleteAccount(id){
	if(confirm("Really want to Delete This Account???\nAll Data related to This Account will Be Deleted!!!")){
		var xhr = new XMLHttpRequest();
		xhr.open("POST","/delete/",true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.send("type=0&id="+id);
		xhr.onreadystatechange = function(){
            if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
                if(xhr.responseText=="1"){
                    alert("Succeed!");
                    document.getElementById("id"+id).style.display = "none";
                }else{
                    alert("Something Wrong!");
                }
			}
		}
	}
}

function deleteProduct(id){
    if(confirm("Really want to Delete This Product???")){
		var xhr = new XMLHttpRequest();
		xhr.open("POST","/delete/",true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.send("type=1&id="+id);
		xhr.onreadystatechange = function(){
            if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
                if(xhr.responseText=="1"){
                    alert("Succeed!");
                    document.getElementById("id"+id).style.display = "none";
                }else{
                    alert("Something Wrong!");
                }
			}
		}
	}
}

function saveAccount(){
    var data = document.getElementsByName("accounts");
	var array = new Array();
	for(var i = 0;i < data.length;i++){
		if(data[i].style.display!="none"){
            var id = data[i].getAttribute("data-id");
			var username = document.getElementById("username"+id).innerText;
			var password = document.getElementById("password"+id).innerText;
			var email = document.getElementById("email"+id).innerText;
			var type = document.getElementById("type"+id).innerText;
			if(type=="admin"){
				type = 0;
			}else if(type=="seller"){
				type = 1;
			}else if(type=="buyer"){
				type = 2;
            }

            array[i] = new Array();
            array[i][0] = id;
            array[i][1] = username;
            array[i][2] = password;
            array[i][3] = email;
            array[i][4] = type;
		}
    }
   
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/modify/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("type=0&data="+JSON.stringify(array))
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                alert("Saved!!!!");
            }else{
                alert("Something Wrong!!!!");
            }
        }
    }
}

function saveProducts(){
    var data = document.getElementsByName("product");
	var array = new Array();
	for(var i = 0;i < data.length;i++){
		if(data[i].style.display!="none"){
            var id = data[i].getAttribute("data-id");
			var productName = document.getElementById("productName"+id).innerText;
			var tradePlace = document.getElementById("tradePlace"+id).innerText;

            array[i] = new Array();
            array[i][0] = id;
            array[i][1] = productName;
            array[i][2] = tradePlace;
		}
    }
   
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/modify/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("type=1&data="+JSON.stringify(array))
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                alert("Saved!!!!");
            }else{
                alert("Something Wrong!!!!");
            }
        }
    }
}

function selectImage(){
    document.getElementById("hideInput").click();
}

function getObjectURL(file) {
	var url = null ;
	if(window.createObjectURL!=undefined) {
		url = window.createObjectURL(file) ;
	}else if(window.URL!=undefined) {
		url = window.URL.createObjectURL(file) ;
	}else if(window.webkitURL!=undefined) {
		url = window.webkitURL.createObjectURL(file) ;
	}
	return url ;
}

function showImage(obj){
    var img = getObjectURL(obj.files[0]);
    document.getElementById("imagebox").style.display="none";
	document.getElementById("pic").style.display = "block";
	document.getElementById("imageShow").src = img;
}

function selectSellType(id){
	var status = document.getElementById(id).checked;
	if(id=="flea"&&status==true){
		document.getElementById("auction").checked = false;
		document.getElementById("endtimebox").style.display = "none";
	}else if(id=="auction"&&status==true){
		document.getElementById("flea").checked=false;
		document.getElementById("endtimebox").style.display="block";
	}else{
		document.getElementById("endtimebox").style.display="none";
	}
}

function addProduct(){
    var image = document.getElementById("hideInput").files[0];
	var productname = document.getElementById("productName").value;
	var price = document.getElementById("productPrice").value;
	var sellerName = document.getElementById("sellerName").value;
	var sellerPhone = document.getElementById("sellerPhone").value;
    var address = document.getElementById("address").value;
    
	if(document.getElementById("flea").checked==true){
		var type = "0";
	}else if(document.getElementById("auction").checked==true){
		var type = "1";
	}else{
		alert("How do you want to Sell?");
		return;
    }
    
	if(image==undefined || productname=="" || price=="" || sellerName=="" || sellerName=="" || sellerPhone=="" || address==""){
		alert("Complete Product Information Please!");
		return;
    }
    
    var fd = new FormData();
	fd.append("img",image);
	fd.append("productname",productname);
	fd.append("price",price);
	fd.append("sellerName",sellerName);
	fd.append("sellerPhone",sellerPhone);
	fd.append("address",address);
    fd.append("type",type);
    
    if(type==1){
		var endtime = document.getElementById("endtime").value;
		fd.append("endtime",endtime);
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/addProduct/",true);
    //xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send(fd);
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                alert("Upload Succeed!");
                window.location.href="/seller/?page=list";
            }else{
                alert("Something Wrong!");
            }
        }
    }
}

function showUploadTable(){
    if(document.getElementById("addProductTable").style.display=="none"){
        document.getElementById("addProductTable").style.display="block";
    }else if(document.getElementById("addProductTable").style.display=="block"){
        document.getElementById("addProductTable").style.display="none";
    }
}

function showSearchingPage(){
    if(document.getElementById("searchbox").style.display=="none"){
        document.getElementById("searchbox").style.display="block";
    }else if(document.getElementById("searchbox").style.display=="block"){
        document.getElementById("searchbox").style.display="none";
    }
}

function addtoCart(id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/deal/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("type=0&id="+id);
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                var go = confirm("Go to Cart to Check it!");
                if(go){
                    window.location.href='/buyer/?page=cart';
                }
            }else if(xhr.responseText=="0"){
                alert("Login Please!");
                window.location.href='/login/';
            }else{
                alert("Something Wrong!");
            }
        }
    }
}

function buy(id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/deal/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("type=1&id="+id);
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                var go = confirm("Get it!");
                if(go){
                    window.location.href='/buyer/?page=list';
                }
            }else if(xhr.responseText=="0"){
                alert("Login Please!");
                window.location.href='/login/';
            }else{
                alert("Something Wrong!");
            }
        }
    }
}

function bid(id,current_price){
    var price = document.getElementById("bidprice").value;
    if(price <= current_price){
        alert("Please Input Your Price above Current Price!");
        return;
    }
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/deal/",true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("type=2&id="+id+"&price="+price);
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
            if(xhr.responseText=="1"){
                var go = confirm("Go to Order Page to Check it!");
                if(go){
                    window.location.href='/buyer/?page=list';
                }
            }else if(xhr.responseText=="0"){
                alert("Login Please!");
                window.location.href='/login/';
            }else{
                alert("Something Wrong!");
            }
        }
    }
}

function connect(){
	var name = document.getElementById("contentname").value;
	var email = document.getElementById("contentemail").value;
	if(document.getElementById("type").value=="buyer"){
		var type = "2";
	}else if(document.getElementById("type").value=="seller"){
		var type = "1";
	}else{
		alert("Please Enter Correct Type!");
		return;
	}
	
	var inner = document.getElementById("inner").value;
	var xhr = new XMLHttpRequest();
	xhr.open("POST","/deal/",true);
	xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xhr.send("type=3&name="+name+"&email="+email+"&utype="+type+"&inner="+inner);
	xhr.onreadystatechange = function(){
		if(xhr.readyState===4){
			if (xhr.readyState == 4 && (xhr.status >= 200 && xhr.status < 400)){
				if(xhr.responseText=="1"){
					alert("Succeed!");
					window.location.href='/homepage/'
				}else{
					alert("Something Wrong!");
				}
			}
		}
	}
}