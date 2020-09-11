function sendPOSTrequest(){
    event.preventDefault();
    deviceID=$('#deviceID').val()
    deviceName=$('#deviceName').val()
    measureType=$('#measureType').val()
    unit=$('#unit').val()
    $.ajax({
        type: "POST",
        url: '/',
        contentType: 'application/json',
        data: JSON.stringify({'deviceID':deviceID,'deviceName':deviceName,"measureType":measureType,"unit":unit}),
        dataType: 'json',
        success:function(response){
          updateTable(response);
        }
      });
}

function updateTable(data){
    var updatedTableBody='';
    for (var i=0;i<data.deviceList.length;i++){
      updatedTableBody+='<tr>';
      device=data.deviceList[i]
      updatedTableBody+="<td>"+device.deviceID+"</td>"+
      "<td>"+device.deviceName+"</td>"+
      "<td>"+device.measureType+"</td>"+
      "<td>"+device.unit+"</td>";
      updatedTableBody+="</tr>";  
    }
    
    $("#tableBody").html(updatedTableBody);
}