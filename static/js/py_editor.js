var original_event;
var editor = {
    layout:{
        starthtml:'<div class="row py-dashed" draggable="true" data-element="Layout" data-select="true" data-cell="Layout" data-eleAdd="true" data-set="{\'gt\':{},\'pt\':{\'layouttype\':\'Single\'},\'at\':{}}"><div class="column c12 h50px" data-removeele="true"></div></div>',
        columnhtml:'<div class="py-dashed column c12" draggable="true" data-select="true" data-cell="Layout" data-type="ColumnLayout"><div class="row py-dashed" data-select="true" data-cell="Layout"  data-element="Layout" data-eleAdd="true" data-set="{\'gt\':{},\'pt\':{\'layouttype\':\'Single\'},\'at\':{}}"><div class="column c12 h50px" data-removeele="true"></div></div></div>'
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
    $(event.target).closest("[data-eleAdd='true']").append(html);
    $(event.target).closest("[data-eleAdd='true']").find('[data-removeele="true"]').first().remove();
}