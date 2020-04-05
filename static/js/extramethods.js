body = $("body");
$(document).on({
    ajaxStart: function() { body.addClass("loading");},
     ajaxStop: function() { body.removeClass("loading"); }
});

function openpopup(html) {
  var myWindow = window.open("", "MsgWindow", "width=500,height=400");
  myWindow.document.write(html);
}

openwindow = function(url, verb, data, target) {
  var form = document.createElement("form");
  form.action = url;
  form.method = verb;
  //form.onsubmit = "processevent(event)"
  form.target = target || "_self";
  if (data) {
    for (var key in data) {
      var input = document.createElement("textarea");
      input.name = key;
      input.value = typeof data[key] === "object" ? JSON.stringify(data[key]) : data[key];
      form.appendChild(input);
    }
  }
  form.style.display = 'none';
  document.body.appendChild(form);
  form.submit();
};

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
   console.log(ev.target,ev.target.dataset.type);
   original_event = ev.target;
  ev.dataTransfer.setData("originevent", ev.target.dataset.type);
}
function enterDrop(event){
      if($(event.target).closest("[data-select='true']").length>0){
        node = event.target
        if(event.target.nodeType==3){// text node verification
            node = event.target.parentNode
        }
        console.log(event.target)
        position = node.closest("[data-select='true']").getBoundingClientRect();
          left = position.left;
          topy = position.top;
          width = position.width;
          //console.log(position);
          $("[data-type='border']").addClass(" displayflex");
              $("[data-type='border']").css({"top":topy,"left":left,"width":width});
        if($(event.target).closest("[data-select='true']").length>0){
              $("[data-type='border']").addClass(" displayflex");
              $("[data-type='border']").css({"top":topy,"left":left,"width":width});
          }
        //$(event.target).closest("[data-select='true']").css({"border-top":""});
        //$(event.target).closest("[data-select='true']").css({"border-top":"5px Solid #0de0d4"});
        //event.target.style.borderTop="5px Solid #0de0d4";
        //$("[data-type='border']").addClass(" displayflex");
        //$("[data-type='border']").css({"width":"100%"});
        //$(event.target).closest("[data-select='true']").toggleClass(" py-comp-select");
        //event.target.closest("[data-select='true']").dataset['current']='true';
    }else{
        $(event.target).css({"border-top":"","border-bottom":""});
        $(event.target).css({"border-top":"5px Solid #0de0d4"});
        //event.target.dataset['current']='true';
    }
}
function leaveDrop(event){
    /*if($(event.target).closest("[data-select='true']").length>0){
        $(event.target).closest("[data-select='true']").css({"border-top":"","border-bottom":""});
    }else{
        $(event.target).css({"border-top":"","border-bottom":""});
        //event.target.dataset['current']='true';
    }*/
    $(event.target).css({"border-top":"","border-bottom":""});
    //$("[data-type='border']").removeClass(" displayflex");
}
function drop(ev) {
  ev.preventDefault();
  $(ev.target).css({"border-top":"","border-bottom":""});
  $("[data-type='border']").removeClass(" displayflex");
  var originevent = ev.dataTransfer.getData("originevent");
  //console.log(originevent);
  if(originevent=="Layout"){
    //addLayout(event);
    pw(event.target).addLayout(event);
  }else if(originevent=="Input"){
    //addcolumn(event,originevent);
    pw(event.target).addinput(event,originevent);
  }else if(originevent=="Label"){
    pw(event.target).addLabel(event,originevent);
  }else if(originevent=="Dropdown"){
    pw(event.target).dropdown(event,originevent);
  }else if(originevent=="CheckBox"){
    pw(event.target).checkbox(event,originevent);
  }else if(originevent=="RadioButton"){
    pw(event.target).RadioButton(event,originevent);
  }else if(originevent=="section"){
    pw(event.target).addsection(event,originevent);
  }else if(originevent=="sectiongroup"){
    pw(event.target).addSectionGroup(event,originevent);
  }else if(originevent=="sectionrepeat"){
    pw(event.target).addSectionRepeat(event,originevent);
  }else if(originevent=="buttonbar"){
    pw(event.target).addbuttonbar(event,originevent);
  }else if(originevent=="button"){
    pw(event.target).addbutton(event,originevent);
  }else if(originevent=="icon"){
    pw(event.target).addIcon(event,originevent);
  }else if(originevent=="repeattable"){
    pw(event.target).addTableRepeat(event,originevent);
  }else if(originevent=="tablecolumn"){
    pw(event.target).addTableColumn(event,originevent);
  }else if(originevent=="menugroup"){
    pw(event.target).addMenuLayout(event,originevent);
  }else if(originevent=="menuitem"){
    pw(event.target).addMenuItem(event,originevent);
  }else if(originevent=="Custom"){
    addCustom(event);
  }else if(originevent=="Column"){
    dropColumn(event);
  }else if(originevent=="ColumnLayout"){
    dropColumnLayout(event);
  }

}



function opensettings(event){
    console.log($(event.data.evt.target));
    $("[data-type='actions']").addClass(" displayNone");
    conf = $(event.data.evt.target).closest("[data-select='true']").attr("data-set");
    id = $(event.data.evt.target).closest("[data-select='true']").attr("id");
    //actionset = {"actionset":[{"event":"click", "eventdata":[{"action":"exeaction", "actionname":"opensettings","config":conf, "id":id},{"action":"modelwindow", "form":"element_settings", "target":"PyModalAAA"}]}]};
    //actionset = {"actionset":[{"event":"click", "eventdata":[{"action":"opensettings"}]}]};
    actionset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    processeventaction((event.data.evt), actionset);
    //processeventaction_another_function(actionset,$(event.data.evt.target));
    //html = generatesettings($(event.data.evt.target));
    //console.log(html);
    //openmodelwindow(event,html);
}
$(document).on("click", ("[data-type='editor']"), function() {
    if(event.target.closest("[data-select='true']")!=null){
          position = event.target.closest("[data-select='true']").getBoundingClientRect();
          //console.log(position);
          positionforoptions = document.body.querySelector("[data-type='actions']").getBoundingClientRect();
          right = position.right;
          topy = position.top;
          targetwidth = document.body.querySelector("[data-type='actions']").clientWidth;
          //targetpo = document.body.querySelector("[data-type='actions']").getBoundingClientRect();
          //console.log(targetpo);
          if(targetwidth<86){
            targetwidth = 86;
          }
          $(".py-comp-selected").removeClass(" py-comp-selected");
          $(event.target).closest("[data-select='true']").addClass(" py-comp-selected");
          $("[data-type='actions']").removeClass(" displayNone");
          $("[data-type='actions']").css({"top":topy-20,"left":right-targetwidth,"cursor":"pointer"});// set location of actions
          $("[data-type='actions']").find(".fa-cog").off("click");// remove click event
          $("[data-type='actions']").find(".fa-cog").on("click",{"evt":event},opensettings);// add click event
    }else{
        $(".py-comp-selected").removeClass(" py-comp-selected");
        $("[data-type='actions']").addClass(" displayNone");
    }
});
$(document).on("blur", ("[data-type='editor']"), function() {
    //console.log($(event.target));
    $(event.target).closest("[data-select='true']").removeClass(" py-comp-selected");
    $("[data-type='actions']").find(".fa-cog").off("click");
});
$(document).on("click", ("[data-type='editor']"), function() {
    console.log($(event.target));
    //$(event.target).closest("[data-select='true']").removeClass(" py-comp-selected");
    //$("[data-type='actions']").find(".fa-cog").off("click");
    pw().setremianheight('sample');
});

function generateid(length) {
   var result           = '';
   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
   var charactersLength = characters.length;
   for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}

function openmodelwindow(event,displayhtml,target){
    if(target==""){target="PyModalAAA"};
    document.getElementById(target).style.display = "block";
    $('#'+target).find('[data-body="true"]').html(displayhtml);
}
function closemodel(event){
    document.getElementById("PyModalAAA").style.display = "none";
}

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}
$(function(){

    // Create overlay and append to body:
    $('<div id="overlay"/>').css({
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height:'100%',
        opacity: .8,
        background: "white url(/media/ajax-loader.gif) no-repeat center"
    }).hide().appendTo('body');
});
// Menu drop down calling
$(document).on("mouseover", ("[data-type='MenuHome']"), function() {
    po = event.target.getBoundingClientRect();
    console.log(po);
    classname = $(event.target).closest("[data-type='Menu']").attr("class");
    if(classname.includes("py-menu-hover")){
        pw().enablemenu(event, "");
        //$("[data-type='actions']").find(".fa-cog").on("click",{"evt":event},opensettings);// add click event
    }
});