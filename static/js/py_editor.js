var original_event;
var editor = {
    layout:{
        starthtml:"<div class='row py-dashed' draggable='true' data-element='Layout' data-select='true' data-cell='Layout' data-eleAdd='true' data-set='{\"gt\":{\"layouttype\":\"Single\", \"visibility\":\"Always\"},\"pt\":{},\"at\":{}}'><div class='column c12 h50px' data-removeele='true'></div></div>",
        columnhtml:"<div class='column c12' draggable='true' data-type='ColumnLayout'><div class='row py-dashed' data-select='true' data-cell='Layout'  data-element='Layout' data-eleAdd='true' data-set='{\"gt\":{\"layouttype\":\"Single\", \"visibility\":\"Always\"},\"pt\":{},\"at\":{}}'>><div class='column c12 h50px' data-removeele='true'></div></div></div>"
    },
    input:{
        starthtml:'<div class="form-group"><label>Default:</label><input type="input" class="form-control"></div>'
    },
    column:{
        starthtml:'<div class="py-dashed column c6 h50px" draggable="true" data-select="true" data-type="Column"',
        attrhtml:'>',
        endhtml:'</div>'
    }
};

function addLayout(event){
    //console.log(event.target);
    if($(event.target).closest("[data-eleAdd='true']").attr("data-element")=="Layout"){
        lay_html = editor.layout.columnhtml;
        console.log(lay_html);
        $(event.target).closest("[data-eleAdd='true']").append(lay_html);
    }else{
        $(event.target).closest("[data-eleAdd='true']").find('[data-removeele="true"]').remove();
        lay_html = editor.layout.starthtml;
        $(event.target).closest("[data-eleAdd='true']").append(lay_html);
    }

}
function dropColumnLayout(event){
    //console.log(original_event);
    $(event.target).closest("[data-eleAdd='true']").append(original_event.innerHTML);
    $(original_event).remove();
    original_event="";
}
function addcolumn(event,type){
    html = editor.column.starthtml;
    if(type=="Input"){
        html += "data-cell='Input'";
        html += editor.column.attrhtml;
        html += editor.input.starthtml;
    }
    html += editor.column.endhtml;
    //console.log(tempDiv.innerHTML);
    console.log($(event.target).closest("[data-eleAdd='true']").length);
    if($(event.target).closest("[data-type='Column']").length>0){
        //console.log("in");
        if($(event.target).attr("data-removeele")=="true"){
            $(event.target).closest("[data-eleAdd='true']").append(html);
        }else{
            $(event.target).closest("[data-type='Column']").after(html);
        }
    }else{
        $(event.target).closest("[data-eleAdd='true']").append(html);
    }
    $(event.target).closest("[data-eleAdd='true']").find('[data-removeele="true"]').first().remove();
}

function dropColumn(event){
    if($(event.target).closest("[data-type='Column']").length>0){
        $(event.target).closest("[data-type='Column']").after(original_event.outerHTML);
        $(original_event).remove();
        original_event="";
    }
}

function generatesettings(parentelement){
    //console.log($(parentelement).closest("[data-select='true']").attr("data-set"));
    dataset = $(parentelement).closest("[data-select='true']").attr("data-set");
    console.log(dataset);
    jsonset = JSON.parse(dataset);
    /*datatabroot = generateid(5);
    var tabsroot = document.createElement("div");
    tabsroot.dataset.tabroot=datatabroot
    var tabtabs = document.createElement("div");
    tabtabs.setAttribute("class","tab");
    tabtabs.dataset.tabs='true';
    var tabcontent = document.createElement("div");
    tabcontent.setAttribute("class","tab");
    tabcontent.dataset.tabcontent='true';
    var i;
    for(i in jsonset){
    console.log(i);
        tabdata = jsonset[i]
        if(!isEmpty(tabdata)){
            tabid = generateid(5);
            var tablinks = document.createElement("button");
            tablinks.setAttribute("class","tablinks active");
            //tablinks.onclick = function(event){opentab(event);};
            tablinks.setAttribute("onclick","opentab(event)");
            tablinks.dataset.target= tabid;
            tablinks.dataset.root = datatabroot;
            var tname;
            if(i=='gt'){
                tname = 'General';
            }else if(i == 'pt'){
                tname = 'Presentation';
            }else{
                tname = 'Actions';
            }
            var tabname = document.createTextNode(tname);
            tablinks.appendChild(tabname);
            var tabcon = document.createElement("div");
            tabcon.id = tabid;
            tabcon.class = "display";
            tabtabs.appendChild(tablinks);
            tabcontent.appendChild(tabcon);
        }
    }
    tabsroot.appendChild(tabtabs);
    tabsroot.appendChild(tabcontent);*/
    return tabsroot.outerHTML;
}