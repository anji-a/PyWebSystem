body = $("body");
$(document).on({
    ajaxStart: function() { body.addClass("loading");},
     ajaxStop: function() { body.removeClass("loading"); }
});

function openpopup(html) {
  var myWindow = window.open("", "MsgWindow", "width=500,height=400");
  myWindow.document.write(html);
}

/*
function openWindow(url="",name="New Window",target="_blank"){
    if(url!=""){
        window.open(url,name,target);
    }
}
*/
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
        position = event.target.closest("[data-select='true']").getBoundingClientRect();
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
    addLayout(event);
  }else if(originevent=="Input"){
    addcolumn(event,originevent);
  }else if(originevent=="Custom"){
    addCustom(event);
  }else if(originevent=="Column"){
    dropColumn(event);
  }else if(originevent=="ColumnLayout"){
    dropColumnLayout(event);
  }

}

$(document).ready(function(){
  $("[data-type='editor']").on({
    mouseover: function(event){
        if(event.target.closest("[data-select='true']")!=null){
            position = event.target.closest("[data-select='true']").getBoundingClientRect();
              //console.log(event.target.closest("[data-select='true']"));
              left = position.left;
              topy = position.top;
              $(event.target).closest("[data-select='true']").addClass(" py-comp-select");
              if($(event.target).closest("[data-select='true']").length>0){
                  $("[data-type='title']").find("h6").text($(event.target).closest("[data-select='true']").attr("data-cell"));
                  $("[data-type='title']").addClass(" displayflex");
                  $("[data-type='title']").css({"top":topy-15,"left":left,"cursor":"pointer"});
              }
        }
    },
    mouseout: function(event){
      $(event.target).closest("[data-select='true']").removeClass(" py-comp-select");
      $("[data-type='title']").removeClass(" displayflex");
    },
    click: function(event){
      if(event.target.closest("[data-select='true']")!=null){
          position = event.target.closest("[data-select='true']").getBoundingClientRect();
          positionforoptions = document.body.querySelector("[data-type='actions']").getBoundingClientRect();
          right = position.right;
          topy = position.top;
          targetwidth = document.body.querySelector("[data-type='actions']").clientWidth;
          //console.log(position,event);
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
    },
    blur: function(event){
        console.log($(event.target));

       $(event.target).closest("[data-select='true']").removeClass(" py-comp-selected");
       $("[data-type='actions']").find(".fa-cog").off("click");
    }
  });
});

function opensettings(event){
    console.log($(event.data.evt.target));
    $("[data-type='actions']").addClass(" displayNone");
    conf = $(event.data.evt.target).closest("[data-select='true']").attr("data-set");
    actionset = {"actionset":[{"event":"click", "eventdata":[{"action":"exeaction", "actionname":"resetsettings_for_element","config":conf},{"action":"modelwindow", "form":"element_settings", "target":"PyModalAAA"}]}]};
    processeventaction_another_function(actionset,$(event.data.evt.target));
    //html = generatesettings($(event.data.evt.target));
    //console.log(html);
    //openmodelwindow(event,html);
}

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