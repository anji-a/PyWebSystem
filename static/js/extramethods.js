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
   //console.log(ev.target,ev.target.dataset.type);
   original_event = ev.target;
  ev.dataTransfer.setData("originevent", ev.target.dataset.type);
}
function enterDrop(event){
    if(event.target.hasChildNodes()){
        if(event.target.innerHTML==$(event.target).closest('[data-element="Layout"]').last().html()){
        console.log(1);
            $(event.target).css({"border-bottom":"5px Solid #0de0d4"});
        }else{
            console.log(2);
            $(event.target).css({"border-top":"5px Solid #0de0d4"});
        }
    }else{
        console.log(3);
        $(event.target).css({"border-top":"5px Solid #0de0d4"});
    }
    event.target.dataset['current']='true';
}
function leaveDrop(event){
    $(event.target).css({"border-top":"","border-bottom":""});
}
function drop(ev) {
  ev.preventDefault();
  $(ev.target).css({"border-top":"","border-bottom":""});
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
          //console.log(document.body.querySelector("[data-type='actions']"));
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