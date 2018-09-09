
function g(id){return document.getElementById(id);}


function showLogDialog(){

   // g("loginBox").style.opacity = "1";
   g("loginBox").style.visibility = "visible";
    g("logimg").style.display = "block";
     $('#Logtip').html("");

}
 
function closeLogDialog(){
	//g("loginBox").style.opacity = "0";
    g("loginBox").style.visibility = "hidden";
    g("logimg").style.display = "none";
}
function showRegDialog(){
	 g("RegisterBox").style.visibility = "visible";
     g("logimg").style.display = "block";
}
function closeRegDialog(){
	g("RegisterBox").style.visibility = "hidden";
	 g("logimg").style.display = "none";
}


function submitLogin(){
  var name=document.getElementById("LogUserName").value;
  var password=document.getElementById("LogPassword").value;
  console.log(name);
  console.log(password);}
 /* var List=JSON.parse('{{ logResult|safe }}');
  for (i in List){
       console.log(i);
    }*/
/*
  $.ajax({
    url:'/login/',
    type:'POST',
    data:{Logusername:name,Logpassword:password},
    success:function(logResult){
        var callback_dict=$.parseJSON(logResult);
        if(callback_dict.status==0){
            $('#Logtip').html("用户名或密码错误")
        }
        else if(callback_dict.status==1){
            alert("登录成功!");
            window.location.href="User.html";
        }

    }
  })
}
*/
function submitRegist(){
  var name=document.getElementById("RegUsername").value;
  var password=document.getElementById("RegPassword").value;
  console.log(name);
  console.log(password);
  var radio=document.getElementsByName("1");
  for(var i=0;i<radio.length;i++)
  {
    if(radio[i].checked)
    {
      console.log(radio[i].value);
    }
  }
}

