
function openWindow(event,dataset){
    //var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    console.log(dataset.location);
    $('#'+dataset.location+'Body').load('UI_Include', dataset);
    //$("#condition").empty();
    //$("#condition").append(rowdiv);
    $('#'+dataset.location).modal({'show':true,backdrop:'static'});
}

function closemodal(location){
    $('#'+location).modal('hide');
}