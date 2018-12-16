
function processrequest(event){
    event.preventDefault();
    var data=$(event.target).closest("form").serializeArray();
    //console.log($(event.target).attr('data-controlset'));
    var datacontrolset=jQuery.parseJSON($(event.target).attr('data-controlset') || '{}');
    data.push({name:'data-controlset',value:datacontrolset});
    //console.log(data);
    $.ajax({ data: data,
        type: $(event.target).closest("form").attr("method"),
        url: $(event.target).closest("form").attr("action"),
        dataType: 'json',

            success: function(response) {
                //alert(3);
                $.each(datacontrolset, function(key,value) {
                  $.each(value,function(key,value){
                    $.each(value,function(key,value){
                        processaction(value,event,response);
                    });
                  });
                });
            },
            error: function (request, status, error) {
                 console.log(request.responseText);
            },
            beforeSend: function() {
                //alert(1);
                //location = $(event.target).closest("[role='dialog']").attr("id");
                //$('#'+location).modal('hide');
            },
            complete: function() {
              // alert(2);

            }
    });
}



function processaction(actionset,event,response){
    if(actionset.action=="Close"){
        var location=$(event.target).closest("[role='dialog']").attr("id");
        //console.log(location);
        closemodal(location);
    }else if(actionset.action=="openwindow"){
        if(actionset.type='tab'){
            actionset.html=response.html;
            addTabByHtml(actionset);
        }
    }
}