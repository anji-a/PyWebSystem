
function openWindow(event,dataset){
    //var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    console.log(dataset.location);
    // data object will contain control set data
    //data = jQuery.parseJSON('{"jType":"ParseJson"}');
    data = $(event.target).serializeArray();
    //data1 = json.loads(dataset)
    data.push({name:'data-controlset',value:JSON.stringify(dataset)});
    console.log(data)
    $('#'+dataset.location+'Body').load('UI_Include', data);
    //$("#condition").empty();
    //$("#condition").append(rowdiv);
    $('#'+dataset.location).modal({'show':true,backdrop:'static'});
}

function closemodal(location){
    $('#'+location).modal('hide');
}