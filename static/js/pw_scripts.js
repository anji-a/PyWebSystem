var domElement = function(selector, context, length) {
 this.selector = selector || null;
 this.context = context || null;
 this.length = length||0;
};

var rootjQuery,

	// A simple way to check for HTML strings
	// Prioritize #id over <tag> to avoid XSS via location.hash (#9521)
	// Strict HTML recognition (#11290: must start with <)
	rquickExpr = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/;
domElement.prototype.init = function(selector, context, root) {
		var match, elem;

		// HANDLE: $(""), $(null), $(undefined), $(false)
		if ( !selector ) {
			return this;
		}

		// init accepts an alternate rootjQuery
		// so migrate can support jQuery.sub (gh-2101)
		root = root || rootjQuery;

		// Handle HTML strings
		if ( typeof selector === "string" ) {
			if ( selector.charAt( 0 ) === "<" &&
				selector.charAt( selector.length - 1 ) === ">" &&
				selector.length >= 3 ) {

				// Assume that strings that start and end with <> are HTML and skip the regex check
				match = [ null, selector, null ];

			} else {
				match = rquickExpr.exec( selector );
			}

			// Match html or make sure no context is specified for #id
			if ( match && ( match[ 1 ] || !context ) ) {

				// HANDLE: $(html) -> $(array)
				if ( match[ 1 ] ) {
					context = context instanceof jQuery ? context[ 0 ] : context;

					// scripts is true for back-compat
					// Intentionally let the error be thrown if parseHTML is not present
					jQuery.merge( this, jQuery.parseHTML(
						match[ 1 ],
						context && context.nodeType ? context.ownerDocument || context : document,
						true
					) );

					// HANDLE: $(html, props)
					if ( rsingleTag.test( match[ 1 ] ) && jQuery.isPlainObject( context ) ) {
						for ( match in context ) {

							// Properties of context are called as methods if possible
							if ( jQuery.isFunction( this[ match ] ) ) {
								this[ match ]( context[ match ] );

							// ...and otherwise set as attributes
							} else {
								this.attr( match, context[ match ] );
							}
						}
					}

					return this;

				// HANDLE: $(#id)
				} else {
					elem = document.getElementById( match[ 2 ] );

					// Check parentNode to catch when Blackberry 4.6 returns
					// nodes that are no longer in the document #6963
					if ( elem && elem.parentNode ) {

						// Handle the case where IE and Opera return items
						// by name instead of ID
						if ( elem.id !== match[ 2 ] ) {
							return rootjQuery.find( selector );
						}

						// Otherwise, we inject the element directly into the jQuery object
						this.length = 1;
						this[ 0 ] = elem;
					}

					this.context = document;
					this.selector = selector;
					return this;
				}

			// HANDLE: $(expr, $(...))
			} else if ( !context || context.jquery ) {
				return ( context || root ).find( selector );

			// HANDLE: $(expr, context)
			// (which is just equivalent to: $(context).find(expr)
			} else {
				return this.constructor( context ).find( selector );
			}

		// HANDLE: $(DOMElement)
		} else if ( selector.nodeType ) {
			this.context = this[ 0 ] = selector;
			this.length = 1;
			return this;

		// HANDLE: $(function)
		// Shortcut for document ready
		} else if ( jQuery.isFunction( selector ) ) {
			return typeof root.ready !== "undefined" ?
				root.ready( selector ) :

				// Execute immediately if ready is not present
				selector( jQuery );
		}

		if ( selector.selector !== undefined ) {
			this.selector = selector.selector;
			this.context = selector.context;
		}

		return jQuery.makeArray( selector, this );
};
domElement.prototype.on = function(event, callback) {
 var evt = this.eventHandler.bindEvent(event, callback, this.element);
}
domElement.prototype.off = function(event) {
 var evt = this.eventHandler.unbindEvent(event, this.element);
}
domElement.prototype.val = function(newVal) {
 return (newVal !== undefined ? this.element.value = newVal : this.element.value);
};
domElement.prototype.append = function(html) {
 this.element.innerHTML = this.element.innerHTML + html;
};
domElement.prototype.prepend = function(html) {
 this.element.innerHTML = html + this.element.innerHTML;
};
domElement.prototype.html = function(html) {
 if (html === undefined) {
 return this.element.innerHTML;
 }
 this.element.innerHTML = html;
};
domElement.prototype.eventHandler = {
 events: [],
 bindEvent: function(event, callback, targetElement) {
 this.unbindEvent(event, targetElement);
 targetElement.addEventListener(event, callback, false);
 this.events.push({
 type: event,
 event: callback,
 target: targetElement
 });
 },
 findEvent: function(event) {
 return this.events.filter(function(evt) {
 return (evt.type === event);
 }, event)[0];
 },
 unbindEvent: function(event, targetElement) {
 var foundEvent = this.findEvent(event);
 if (foundEvent !== undefined) {
 targetElement.removeEventListener(event, foundEvent.event, false);
 }
 this.events = this.events.filter(function(evt) {
 return (evt.type !== event);
 }, event);
 }
};

domElement.prototype.addLayout = function(event){
    console.log(this, $(event.target));
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    //starthtml="<div class='w3-row py-dashed' draggable='true' data-element='Layout' id="+layid+" data-select='true' data-cell='Layout' data-eleAdd='true' data-set='{\"General\":{\"containerformat\":\"Default\", \"layoutformat\":\"inline\", \"visibility\":\"Always\" , \"deferload\":\"deferload\"},\"Presentation\":{\"flot\":\"Left\",\"style\":\"deferload\",\"css\":\"deferload\"},\"Action\":{}}'><div class='column c12 h50px' data-removeele='true'></div></div>";
    starthtml = '<div class="w3-row" draggable="true" data-element="LayoutGroup" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="Layout" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Layout</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Drag Elements Here</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='ColumnLayout'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }

    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection"){
        // no need to add anything
    }else{
        lay_html = starthtml;
        console.log(lay_html);
        $(this).closest("[data-eleAdd='true']").append(lay_html);
    }

}
domElement.prototype.addMenuLayout = function(event){
    console.log(this, $(event.target));
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    //starthtml="<div class='w3-row py-dashed' draggable='true' data-element='Layout' id="+layid+" data-select='true' data-cell='Layout' data-eleAdd='true' data-set='{\"General\":{\"containerformat\":\"Default\", \"layoutformat\":\"inline\", \"visibility\":\"Always\" , \"deferload\":\"deferload\"},\"Presentation\":{\"flot\":\"Left\",\"style\":\"deferload\",\"css\":\"deferload\"},\"Action\":{}}'><div class='column c12 h50px' data-removeele='true'></div></div>";
    starthtml = '<div class="w3-row" draggable="true" data-element="MenuGroup" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="MenuGroup" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Menu Group</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Drag Menu Elements Here</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='ColumnMenuGroup'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }

    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection"){
        // no need to add anything
    }else{
        lay_html = starthtml;
        console.log(lay_html);
        $(this).closest("[data-eleAdd='true']").append(lay_html);
    }

}
domElement.prototype.addSectionGroup = function(event){
    console.log(this, $(event.target));
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    //starthtml="<div class='w3-row py-dashed' draggable='true' data-element='Layout' id="+layid+" data-select='true' data-cell='Layout' data-eleAdd='true' data-set='{\"General\":{\"containerformat\":\"Default\", \"layoutformat\":\"inline\", \"visibility\":\"Always\" , \"deferload\":\"deferload\"},\"Presentation\":{\"flot\":\"Left\",\"style\":\"deferload\",\"css\":\"deferload\"},\"Action\":{}}'><div class='column c12 h50px' data-removeele='true'></div></div>";
    starthtml = '<div class="w3-row" draggable="true" data-element="SectionGroup" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="SectionGroup" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Section Group</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Drag Section Elements Here</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='SectionGroup'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }

    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection"){
        // no need to add anything
    }else{
        lay_html = starthtml;
        console.log(lay_html);
        $(this).closest("[data-eleAdd='true']").append(lay_html);
    }

}
domElement.prototype.addinput = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            input_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="Input"><label>Default:</label><input type="input" class="w3-input w3-border"></div>';
            $(ele).append(input_html);
            console.log(input_html);
        }
    }
}

domElement.prototype.addLabel = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            label_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="Label"><label>Enter label:</label></div>';
            $(ele).append(label_html);
            console.log(label_html);
        }
    }
}
domElement.prototype.addMenuItem = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            label_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="MenuItem"><label>Menu Item</label></div>';
            $(ele).append(label_html);
            console.log(label_html);
        }
    }
}
domElement.prototype.dropdown = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            dropdown_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="select"><label>Select From List</label><select class="w3-select w3-border"><option selected>Select..</option></select></div>';
            $(ele).append(dropdown_html);
            console.log(dropdown_html);
        }
    }
}
domElement.prototype.checkbox = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            checkbox_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="CheckBox"><label>Please select your option</label><input class="w3-check" type="checkbox"><label>Check Box</label></div>';
            $(ele).append(checkbox_html);
            console.log(checkbox_html);
        }
    }
}
domElement.prototype.addbutton = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="ButtonBar" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            button_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="button"><button class="w3-button w3-green">Button</button></div>';
            $(ele).append(button_html);
            console.log(button_html);
        }
    }
}
domElement.prototype.addIcon = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="ButtonBar" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="MenuGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            button_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="icon"><i class="fa fa-plus fa-lg"></i></div>';
            $(ele).append(button_html);
            console.log(button_html);
        }
    }
}
domElement.prototype.addTableColumn = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatTable"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            button_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="tablecolumn"><label>Table Column</label></div>';
            $(ele).append(button_html);
            console.log(button_html);
        }
    }
}
domElement.prototype.RadioButton = function(event,originevent){
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            RadioButton_html = '<div class="w3-col py-dashed" draggable="true" data-select="true" data-type="Column" data-cell="radio"><label>Select Radio</label><input class="w3-radio" type="radio" checked><label>Radio</label></div>';
            $(ele).append(RadioButton_html);
            console.log(RadioButton_html);
        }
    }
}
domElement.prototype.addbuttonbar = function(event, originevent){
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    starthtml = '<div class="w3-row" draggable="true" data-element="ButtonBar" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="ButtonBar" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Button Bar</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Add Buttons</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='ButtonBar'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }
    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup"){
        // no need to add anything
    }else{
        // no need to add anything
    }
}
domElement.prototype.addSectionRepeat = function(event, originevent){
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    starthtml = '<div class="w3-row" draggable="true" data-element="RepeatSection" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="RepeatSection" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Repeat Section</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Drag Section Elements Here</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='RepeatSection'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }
    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup"){
        // no need to add anything
    }else{
        lay_html = starthtml;
        console.log(lay_html);
        $(this).closest("[data-eleAdd='true']").append(lay_html);
    }
}
domElement.prototype.addTableRepeat = function(event, originevent){
    layid = this.generateid(10);
    colid = this.generateid(10);
    console.log(layid)
    starthtml = '<div class="w3-row" draggable="true" data-element="RepeatTable" data-displaytype="Layout" id="'+layid+'" data-select="true" data-eleAdd="true" data-cell="RepeatTable" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Repeat Section</legend><div data-element="Layout"  data-row="true" data-cellformat="double"><div class="w3-col" data-removeele="true">Drag Section Elements Here</div></div></fieldset></div>'
    columnhtml="<div class='w3-col' draggable='true' id="+colid+" data-type='RepeatTable'>"+starthtml+"</div>";
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup"){
        console.log($(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]);
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            lay_html = columnhtml;
            $(ele).append(lay_html);
            console.log(lay_html);
        }
    }else if ($(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup"){
        // no need to add anything
    }else{
        lay_html = starthtml;
        console.log(lay_html);
        $(this).closest("[data-eleAdd='true']").append(lay_html);
    }
}
domElement.prototype.addsection = function(event,originevent){
    secid = this.generateid(10);
    addsection_html = '<div class="w3-row" draggable="true" data-element="section" data-displaytype="section" id="'+secid+'" data-select="true" data-cell="section" data-name="" data-set="{}"><fieldset class="w3-border-dashed" ><legend>Section</legend><div data-element="section"  data-row="true" data-cellformat="double"> Add Section Details </div></fieldset></div>';
    if($(this).closest("[data-eleAdd='true']").attr("data-element")=="LayoutGroup" ||  $(this).closest("[data-eleAdd='true']").attr("data-element")=="SectionGroup" || $(this).closest("[data-eleAdd='true']").attr("data-element")=="RepeatSection"){
        addcolsection_html = '<div class="w3-col" draggable="true" data-select="true" data-type="SectionColumn" data-cell="section">'+addsection_html+'</div>';
        if(!(isEmpty($(this).closest("[data-eleAdd='true']").find("[data-row='true']")))){
            ele = $(this).closest("[data-eleAdd='true']").find("[data-row='true']")[0]
            $(ele).children('[data-removeele="true"]').remove();
            $(ele).append(addcolsection_html);
            console.log(addcolsection_html);
        }
    }else{
        $(this).closest("[data-eleAdd='true']").append(addsection_html);
    }
}
domElement.prototype.saveelementsettings = function(id, config){
    console.log($(id), config);
    $(id).attr('data-set', JSON.stringify(config))
}
domElement.prototype.isEmpty = function(obj){
    return Object.keys(obj).length === 0;
}

domElement.prototype.generateid = function(length){
   var result           = '';
   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
   var charactersLength = characters.length;
   for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}
domElement.prototype.refreshsection = function(id, html){
    document.getElementById(id).outerHTML = html;
}
domElement.prototype.openAccordion = function(event, id){
    body = document.getElementById(id);
    accordian = $(event.target)
    console.log(accordian);
    if (body.className.indexOf("w3-show") == -1) {
      body.className += " w3-show";
      accordian.removeClass(" w3-black");
      accordian.addClass(" active");
    } else {
      body.className = body.className.replace("w3-show", "");
      accordian.removeClass(" active");
      accordian.addClass(" w3-black");
    }
}
domElement.prototype.enablemenu = function(event, display){
        po = event.target.getBoundingClientRect();
        console.log($(event.target).parent().parent()[0].getBoundingClientRect());
        parentnode_po = $(event.target).closest("[data-type='Menu']").parent()[0].getBoundingClientRect();
            menugroup = $(event.target).closest("[data-type='Menu']").find("[data-type='MenuGroup']")[0];
            direction = $(menugroup).attr("data-direction");
            child_width = menugroup.getBoundingClientRect().width;
            child_height = menugroup.getBoundingClientRect().height;
            x=y=z=0
            if(direction=="" || direction=="Down"){
                x = 0;
                y = po.height;
                z = 0;
            }else if(direction=="Up"){
                x = 0;
                y = -(child_height);
                z = 0;
            }else if(direction=="DownRight"){
                x = po.width;
                y = 0;
                z = 0;
            }
            else if(direction=="DownLeft"){
                if(child_width>po.width){
                    width = child_width
                }else{
                    width = po.width
                }
                x = -width;;
                y = 0;
                z = 0;
            }else if(direction=="UpRight"){
                x = po.width;
                y = -(child_height-po.height);
                z = 0;
            }else if(direction=="UpLeft"){
                if(child_width>po.width){
                    width = child_width
                }else{
                    width = po.width
                }
                x = -width;
                y = -(child_height-po.height);
                z = 0;
            }
            console.log(x,y,z, direction);
            if(display != ""){
            st = "position: absolute;transform: translate3d("+x+"px, "+y+"px, "+z+"px);left: 0px;top:0px;will-change: transform;display:"+display
            }else{
             st = "position: absolute;transform: translate3d("+x+"px, "+y+"px, "+z+"px);left: 0px;top:0px;will-change: transform;"
            }
            menugroup.style = st
            //console.log(menugroup, menugroup.getBoundingClientRect());
}
domElement.prototype.setremianheight = function(id){
    element = document.getElementById(id);
    elechaild = $(element).find("[data-eleAdd='true']")[0];
    po = elechaild.getBoundingClientRect();
    console.log(po);
    topx = po.top;
    if(po.top<100){
        topx = 200;
        console.log(topx);
    }
    Height = window.innerHeight - topx - 30;
    elechaild.style = "height:"+Height;
    console.log(Height);
}
domElement.prototype.geteventdata = function(event, dataset){
    //var dataset = jQuery.parseJSON($(event.target).attr("data-controlset") || '{}');
    var eventdata1 = {};
    console.log(event.target);
    //Object.values(action.actionset[0].eventdata).indexOf("Close")
    for (var eventkey in dataset.actionset) {
        console.log(dataset.actionset[eventkey]);
        for (var key in dataset.actionset[eventkey].eventdata){
            dataset.actionset[eventkey].eventdata[key]["actiondata"]={}
            if(dataset.actionset[eventkey].eventdata[key].action=="refreshsection" || dataset.actionset[eventkey].eventdata[key].action=="previewelement"){
                dataset.actionset[eventkey].eventdata[key]["actiondata"].refreshid = $(event.target).closest("[data-uitype='section']").attr("id");
                dataset.actionset[eventkey].eventdata[key]["actiondata"].refreshnode = $(event.target).closest("[data-uitype='section']").attr("data-node");
                dataset.actionset[eventkey].eventdata[key]["actiondata"].refreshsection = $(event.target).closest("[data-uitype='section']").attr("data-elementname");
            }
            if(dataset.actionset[eventkey].eventdata[key].action=="deleterow"){
                dataset.actionset[eventkey].eventdata[key]["actiondata"].path = $(event.target).closest("[data-uitype='row']").attr("data-path");
            }
            if(dataset.actionset[eventkey].eventdata[key].action=="addrow"){
                dataset.actionset[eventkey].eventdata[key]["actiondata"].path = $(event.target).closest("[data-uitype='rowgroup']").attr("data-path");
            }if(dataset.actionset[eventkey].eventdata[key].action=="opensettings"){
                dataset.actionset[eventkey].eventdata[key]["actiondata"].id = $(event.target).closest("[data-select='true']").attr("id");
                dataset.actionset[eventkey].eventdata[key]["actiondata"].config = $(event.target).closest("[data-select='true']").attr("data-set");
                dataset.actionset[eventkey].eventdata[key]["actiondata"].elementType = $(event.target).closest("[data-select='true']").attr("data-element");
            }
            if(dataset.actionset[eventkey].eventdata[key].action=="refreshothersection"){
                rootelement = $(event.target).closest("[data-find='rootelement']");
                secname = dataset.actionset[eventkey].eventdata[key].sectioname
                sectionlist = rootelement.find("[data-elementname='"+secname+"']");
                sectionarray = []
                $( sectionlist ).each(function( index ) {
                    section = {}
                    section["refreshid"] = $( this ).attr("id");
                    section["refreshnode"] = $( this ).attr("data-node");
                    section["refreshsection"] = secname
                    sectionarray.push(section)
                });
                dataset.actionset[eventkey].eventdata[key]["actiondata"] = sectionarray
                console.log(sectionlist, sectionarray);
            }
            if(dataset.actionset[eventkey].eventdata[key].action=="closeTab"){
                tabdetails = getWorkTabData(event);
                dataset.actionset[eventkey].eventdata[key]["actiondata"] = tabdetails;
            }
        }
    }
    //return eventdata1;
}
pw = function(selector, context) {
 var el = new domElement(selector, context);
 el.init(selector, context);
 //console.log(el)
 return el;
}
