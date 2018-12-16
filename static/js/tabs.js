$( function() {

    var tabs = $( "#workTabs" ).tabs();
    tabs.find("ul[data-tabid='workTabs']" ).sortable({
      axis: "x",
      stop: function() {
        tabs.tabs( "refresh" );
      }
    });

    $(document).on('click','#close-tab',function(){

        //var tabs=$(event.target).tabs();
        //console.log(tabs);
        tabsLocation=$(event.target).attr('data-location');
        //console.log($(event.target));
        var tabs=$('#'+tabsLocation).tabs();
        var panelId = $( this ).closest( "li" ).attr( "aria-controls" );
        //console.log($( this ));
        //console.log(panelId)
        var tabIndex=id2Index('#'+tabsLocation,'#'+panelId)
        //console.log(id2Index('#'+tabsLocation,'#'+panelId));
        //$("#"+panelId).prev().attr('aria-hidden','true')
        $( this ).closest( "li" ).remove();
        $( "#" + panelId ).remove();
        //$("#"+panelId).prev().addClass("ui-tabs-active ui-state-active");
        //tabs.tabs( "option", "active", 0 );
        tabs.tabs("refresh");
        //var tabCount=$('#'+tabsLocation).find(".ui-icon-close").length;
        $('#'+tabsLocation).tabs("option","active",tabIndex-1);
    });

});

function addTab(event,dataSet){
    //console.log($(event.target).attr('data-controlset'));
    //var dataSet = jQuery.parseJSON($(event.target).attr('data-controlset'));
    var tabs=$('#'+dataSet["location"] || "").tabs();
    var id = dataSet.element,
        li = "<li><a href='#"+id+"'>"+id+"</a> <span data-location='"+dataSet["location"]+"' class='ui-icon ui-icon-close' id= 'close-tab' role='presentation'>Remove Tab</span></li>",
        tabContentHtml = id;
        //html = $.parseHTML( tabContentHtml );
       if($("#"+id).length==0){
            tabs.find( "ul[data-tabid='"+dataSet["location"]+"']" ).append( li );
            tabs.append( "<div id='" + id + "'></div>" );
            //tabs.append(tabContentHtml);
            $('#'+id).load('UI_Include', dataSet);

            //includeHTML();
            //$('#'+id).addClass('h95 paddingZero');
            tabs.tabs("refresh");

            //$('#'+$(event.target).attr('data-location')).tabs("option","active",1);
            tabs.tabs("option","active",id2Index('#'+dataSet["location"] || '','#'+id));
       }
}

function addTabByHtml(dataSet){
    var tabs=$('#'+dataSet["location"] || "").tabs();
    var id = dataSet.element,
        li = "<li><a href='#"+id+"'>"+id+"</a> <span data-location='"+dataSet["location"]+"' class='ui-icon ui-icon-close' id= 'close-tab' role='presentation'>Remove Tab</span></li>",
        tabContentHtml = id;
        //html = $.parseHTML( tabContentHtml );
       if($("#"+id).length==0){
            tabs.find( "ul[data-tabid='"+dataSet["location"]+"']" ).append( li );
            tabs.append( "<div id='" + id + "'></div>" );
            //tabs.append(tabContentHtml);
            //$('#'+id).load('UI_Include', dataSet);
            $('#'+id).html(dataSet.html);
            //includeHTML();
            //$('#'+id).addClass('h95 paddingZero');
            tabs.tabs("refresh");

            //$('#'+$(event.target).attr('data-location')).tabs("option","active",1);
            tabs.tabs("option","active",id2Index('#'+dataSet["location"] || '','#'+id));
       }
}
//tabsId Id of the div containing the tab code.
//srcId Id of the tab whose id you are looking for
function id2Index(tabsId, srcId)
{
	var index=-1;
	var i = 0, tbH = $(tabsId).find("li a");
	var lntb=tbH.length;
	if(lntb>0){
		for(i=0;i<lntb;i++){
			o=tbH[i];
			if(o.href.search(srcId)>0){
				index=i;
			}
		}
	}
	return index;
}

// Used to close the tab

function closeActiveTab(Panal){
    var TabId = $('#'+Panal).find('li[aria-selected=true]').attr('aria-controls');
                        //var liele = $('#'+controlData.responseData.datalocation).find("aria-controls:contains("+panelId+")")
    var liele = $("li[aria-controls="+TabId+"]").remove();
    console.log(liele)

    //console.log(tabs.closest("li"));
    //$("#"+panelId).prev().attr('aria-hidden','true')

    $( "#" + TabId ).remove();

}
