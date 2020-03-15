/*  Used to process the from submit through Ajax call */
function processrequest(event){
    event.preventDefault();
    $('#overlay').show();
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
                $('#overlay').hide();
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

function processeventaction(event, actionset="None"){
    $('#overlay').show();
    //event.preventDefault();
    console.log(event);
    if(actionset == "None"){
        var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    }else{
        var dataset = actionset
    }
    var targetnode = $(event.target).closest("[data-find='rootelement']").attr("data-node");// used to find portal type
    var targetthread = $(event.target).closest("[data-find='rootelement']").attr("data-thread");// used to find the user thread
    dataset.threadName = targetthread
    dataset.root_node = targetnode;
    dataset.eventtype = event.type;
    pw().geteventdata(event, dataset)// set action data for each event
    //console.log(dataset);
    //dataset.refershid = $(event.target).closest("[data-uitype='section']").attr("id");// used for refresh section
    //dataset.refreshnode = $(event.target).closest("[data-uitype='section']").attr("data-node");// used for refresh section
    //dataset.refreshnodes =
    //dataset.roothtml = $(event.target).closest("[id='pw_new_purpose']");
    // need to update pw_new_purpose with dynamic element value
    var id =$(event.target).closest("[data-html='true']").attr("id");
    var elem = document.getElementById(id);
    data = {}
    if(elem != null && elem !== undefined ){
        console.log(elem.outerHTML);
        //da = $(event.target).closest("[data-uitype='form']").find("input,select,textarea").serializeArray();
        data = serializeArray(elem);
        //console.log(da);
        if(true){dataset.roothtml = elem.outerHTML;}// need to change logic for get entire html
    }

    if(isEmpty(data)){
        data = $(event.target).serializeArray();
        //data = serializeArray(elem);
    }
        //data = $(event.target).serializeArray();
        //data1 = json.loads(dataset)
    data.push({name:'data-controlset',value:JSON.stringify(dataset)});
    console.log(data);
     $.ajax({ data: data,
        type: "POST",
        url: "/UI_Include",
        dataType: 'json',

            success: function(response) {
                //alert(3);
                console.log(response);
                html = response.html;
                console.log(html);
                eval(html);
                $('#overlay').hide();

            },
            error: function (request, status, error) {
                 console.log(request.responseText);
                 $('#overlay').hide();
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


function processeventaction_another_function(dataset,target){
    /*var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    var targetdata = $(event.target).closest("[data-find='data_root']").attr("data-element");// used to find portal type

    dataset.root_data = targetdata;
    dataset.eventtype = event.type;
    console.log(dataset);*/
    $('#overlay').show();
    var targetnode = $(target).closest("[data-find='rootelement']").attr("data-node");// used to find portal type
    var targetthread = $(target).closest("[data-find='rootelement']").attr("data-thread");// used to find the user thread
    dataset.root_node = targetnode;
    dataset.threadName = targetthread
    dataset.eventtype = event.type;
    data = {}
    //console.log($(event))
    data['data-controlset']=JSON.stringify(dataset);

     $.ajax({ data: data,
        type: "POST",
        url: "/UI_Include",
        dataType: 'json',

            success: function(response) {
                //alert(3);
                console.log(response);
                html = response.html;
                console.log(html);
                eval(html);
                $('#overlay').hide();
            },
            error: function (request, status, error) {
                 console.log(request.responseText);
                 $('#overlay').hide();
            },
            beforeSend: function() {

            },
            complete: function() {

            }
    });

}