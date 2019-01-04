

function processevent(event){
    var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    var targetdata = $(event.target).closest("[data-find='data_root']").attr("data-element");
    console.log(targetdata)
    dataset.root_data = targetdata;
    console.log(dataset)
    if(true){
        data = $(event.target).serializeArray();
        //data1 = json.loads(dataset)
        data.push({name:'data-controlset',value:JSON.stringify(dataset)});
        $('#PWModalBody').load('UI_Include', data);

    }
    else if(dataset.actiontype=="modal"){
        openWindow(event,dataset);
    }else if(dataset.actiontype=="tab"){
        addTab(event,dataset);
    }else if(dataset.actiontype=="window"){
        //openWindow("/processrequest")
        //console.log(dataset);

        open('memory_check','POST', dataset ,'newwin');
    }else if(dataset.event_set[0].action=="refresh_ui"){
        console.log(dataset.event_set[0].action)
        data = $(event.target).serializeArray();
        //data1 = json.loads(dataset)
        data.push({name:'data-controlset',value:JSON.stringify(dataset)});
        // data will hold control set data
        $('#'+dataset.event_set[0].target).load(location.href + ' #'+dataset.event_set[0].target+'>*', data);
    }

}