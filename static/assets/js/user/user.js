function getCookie(name) {
    let cookieValue = "all";
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submit_login()
{
    // alert("test")
    username=document.getElementById("username").value;
    password=document.getElementById("password").value;

    form={
        "username":username,
        "password":password
    }
    // console.log("form ",form);

    url="http://127.0.0.1:8000/host_to_heroku_login_form/submit/"
    axios({
        method:"POST",
        url:url,
        data:JSON.stringify(form),
        headers:{'content-type':'application/json','X-CSRFToken':getCookie("csrftoken")}
    }).then(function(response){
        new_url=response['data']['base_url'];
        status=response['data']['status'];
        message=response['data']['message'];
        console.log("response['data']['base_url']=",new_url);
        console.log("response['data']['status']=",status);
        if(status==200){
            window.location.replace(new_url);
        }
        else{
            error=document.getElementById("error");
            error.innerHTML=message
        }
    })
    return;
}

// submit_login=document.getElementById("submit_login");
// submit_login.addEventListener("submit",e=>{
//     alert("test");
//     e.preventDefault();
  
// })