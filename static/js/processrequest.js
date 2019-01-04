/*  Used to process the from submit through Ajax call */
function processrequest(event){
    event.preventDefault();
    var data=$(event.target).closest("form").serializeArray();
    var targetdata = $(event.target).closest("[data-find='data_root']").attr("data-element");
    //console.log($(event.target).closest(["data-element"]));
    var datacontrolset=jQuery.parseJSON($(event.target).attr('data-controlset') || '{}');
    datacontrolset.root_data = targetdata;
    datacontrolset.eventtype = event.type;
    data.push({name:'data-controlset',value:JSON.stringify(datacontrolset)});
    data.push({name:'root_data',value:targetdata});
    console.log(datacontrolset);
    //$('#loader3', form).html('<img src="../../images/ajax-loader.gif" />       Please wait...');
    $.ajax({ data: data,
        type: $(event.target).closest("form").attr("method"),
        url: $(event.target).closest("form").attr("action"),
        dataType: 'json',

            success: function(response) {
                //alert(3);
                console.log(response);
                html = response.html;
                //console.log(html);
                eval(html);
                /*$.each(datacontrolset, function(key,value) {
                    if(jQuery.type(value)=="object"){
                        //console.log(".............")
                        $.each(value,function(key,value){
                            //console.log(jQuery.type(value))
                            if(jQuery.type(value)=="array"){
                                //console.log("///////////")
                                $.each(value,function(key,value){
                                    processaction(value,event,response);
                                });
                            }
                      });
                    }
                });*/
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


/* used to process the response from the processrequest(event) function */
function processaction(actionset,event,response){
    if(actionset.action=="Close"){
        var location=$(event.target).closest("[role='dialog']").attr("id");
        console.log(location);
        closemodal(location);
    }else if(actionset.action=="openwindow"){
        if(actionset.type='tab'){
            actionset.html=response.html;
            addTabByHtml(actionset);
        }
    }
}

function processeventaction(event){
    console.log(event);
    var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    var targetdata = $(event.target).closest("[data-find='data_root']").attr("data-element");

    dataset.root_data = targetdata;
    dataset.eventtype = event.type;
    console.log(dataset)
    data = $(event.target).serializeArray();
        //data1 = json.loads(dataset)
    data.push({name:'data-controlset',value:JSON.stringify(dataset)});

     $.ajax({ data: data,
        type: "POST",
        url: "/UI_Include",
        dataType: 'json',

            success: function(response) {
                //alert(3);
                console.log(response);
                html = response.html;
                //console.log(html);
                eval(html);

            },
            error: function (request, status, error) {
                 console.log(request.responseText);
            },
            beforeSend: function() {

            },
            complete: function() {

            }
    });

    /*
    if(true){
        data = $(event.target).serializeArray();
        //data1 = json.loads(dataset)
        data.push({name:'data-controlset',value:JSON.stringify(dataset)});
        $('#PWModalBody').load('UI_Include', data);

    }*/
}
