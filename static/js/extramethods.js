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
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
$(document).ready(function(){
  $(".py-dashed:last").on("mouseenter", function(event){
    console.log($(event.target));
    alert("hi");
  });
});
