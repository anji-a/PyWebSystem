function addchild(e){
    console.log($(jQuery.data(document.body, "parent")).closest("[data-find='row']").children(".col-12").children(".row.no-gutters.pl-5").children("[data-find='row-child-collapse']"))
    $(jQuery.data(document.body, "parent")).closest("[data-find='row']").children(".col-12").children(".row.no-gutters.pl-5").children("[data-find='row-child-collapse']").children("[class='card card-body p-0']").append('<div class="col-12"><div class="row p-1 justify-content-end" data-find="row" data-controlset={"begin-condition":[{"condition":"x=10"},{"condition":"y=10"}]}><div class="col-12"><div class="row m-0"><div class="col-5 p-1"><div class="row m-0"><div class="col-1 p-1"><div class="row no-gutters"><div class="col"><span class="fa fa-caret-right" style="font-size:30px" data-toggle="collapse" onclick=expandrow(event)  role="button" aria-expanded="false" ></span></div><div class="col"><label data-find="sno">1</label></div></div></div><div class="col-2 p-1"><input data-find="jump" type="text" style="width:inherit"/></div><div class="col-2 p-1"><input data-find="condition" type="button" value="Cond" style="width:inherit"  onclick=openConditionWindow(event,"begin-condition")></div><div class="col-2 p-1"><input data-find="loop" type="button" value="For" style="width:inherit" onclick=openForWindow(event,"loop")></div><div class="col-5 p-1"><input data-find="scope" type="text" style="width:inherit" alt="Scope"/></div></div></div><div class="col-6 p-1">   <div class="row m-0"><div class="col-6 p-1"><div class="row m-0"><div class="col-1 p-0"><span class="fa fa-caret-right" style="font-size:30px" data-toggle="collapse" onclick=expandMethod(event)  role="button" aria-expanded="false" ></span></div><div class="col-11 p-0"><input data-find="method" type="text" style="width:inherit" alt="Method"/></div></div></div><div class="col-6 p-1"><input data-find="description" type="text" style="width:inherit" alt="Description"/></div></div></div><div class="col-1 p-1"><div class="row m-0"><div class="col-10 p-1"><input data-find="postcondition" type="button" value="Cond" style="width:inherit" onclick=openConditionWindow(event,"end-condition")></div><div class="col-2 p-1"><h4><a class="fa fa-trash" aria-hidden="true" onclick=removeElement(event) href="#"></a></h4></div></div></div></div><div class="row no-gutters"><!-- Collapse Example --><div class="collapse col-12" data-find="row-collapse">  <div class="card card-body">Empty Section </div></div></div><div class="row no-gutters pl-5"><!-- Collapse Example --><div class="collapse col-12" data-find="row-child-collapse"><div class="card card-body p-0"></div></div></div></div></div>');
    $(jQuery.data(document.body, "parent")).closest("[data-find='row']").children(".col-12").children(".row.no-gutters.pl-5").children("[data-find='row-child-collapse']").collapse('show');
    defineContext();
}

function removeElement(e){
    $(e.target).closest("[data-find='row']").closest(".col-12").remove();
    $(e.target).closest("[data-find='row']").remove();
}

function removeCondition(e){
    //$(e.target).closest("[data-find='row']").closest(".col-12").remove();
    $(e.target).closest("[class='row']").remove();
}

function expandrow(e){
    if ($(e.target).attr("class")=="fa fa-caret-right"){
        $(e.target).attr("class","fa fa-caret-down");
        $(e.target).closest("[data-find='row']").children(".col-12").children(".row.no-gutters.pl-5").children("[data-find='row-child-collapse']").collapse('show');
    }else{
        $(e.target).attr("class","fa fa-caret-right");
        $(e.target).closest("[data-find='row']").children(".col-12").children(".row.no-gutters.pl-5").children("[data-find='row-child-collapse']").collapse('hide');
    }

}


