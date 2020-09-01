function sendPOSTrequest(){
   // event.preventDefault();
    console.log($('#exampleInputEmail1').val())
    username=$('#exampleInputEmail1').val()
    password=$('#exampleInputPassword1').val()
    $.ajax({
        type: "POST",
        url: '/',
        contentType: 'application/json',
        data: JSON.stringify({'username':username,'password':password}),
        dataType: 'json'
      });
}