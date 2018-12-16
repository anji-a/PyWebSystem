
function processevent(event){
    //console.log($(event.target).attr("data-controlset"));
    var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    if(dataset.actiontype=="modal"){
        openWindow(event,dataset);
    }else if(dataset.actiontype=="tab"){
        addTab(event,dataset);
    }
}