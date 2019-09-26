var pytab = {
    tabname : '',
    tablocation : '',
    addtab(event, tab){
        tabgroup = $(event.target).closest('[data-target="py-home-tab"]');

        tabs = tabgroup.find(".tab");

        id= 'dsd';
        name= tab.tabname;
        tabs.append('<button class="tablinks" data-target="'+id+'" onclick="opentab(event)">'+ name+' <span class="topright" onclick="closeTab(event)">&times</span></button>')
        tabgroup.append('<div id="'+id+'" class="tabcontent">'+tab.tabconteent+'</div>');
        console.log(tabgroup.find(".tabcontent"));
        tab = {'tbt':id,'tbg':tabgroup};
        console.log(tab)
        this.opentab(tab);
    },
    opentab(tab){
    console.log(tab);
        tabtarget = tab.tbt
        tabgroup = tab.tbg
        $('#'+tabtarget).removeClass(" nodisplay").addClass(" display");

        $(tabgroup.find(".tablinks")).each(function(){
            i = $( this );
            if(tabtarget== i.attr("data-target")){
                i.addClass(" active");
            }else{
                $('#'+i.attr("data-target")).removeClass(" display").addClass(" nodisplay");
                i.removeClass(" active");
            }
        });

    },
    removetab(tab){
        tabgroup = tab.tbg;
        tabtarget= tab.tbt.attr("data-target");
        var previoustab;
        $(tabgroup.find(".tablinks")).each(function(){
            i = $( this );
            if(tabtarget== i.attr("data-target")){
                if(i.attr("class").includes("active")){
                    $('#'+tabtarget).remove();
                    tab.tbt.remove();
                    console.log(previoustab, previoustab.attr("data-target"))
                    previoustab.addClass(" active");
                    $('#'+previoustab.attr("data-target")).removeClass(" nodisplay").addClass(" display");
                }else{
                    $('#'+tabtarget).remove();
                    tab.tbt.remove();
                }
             }else{
                previoustab = $( this );
            }
        });

    }
}

function opentab(evt){
    tabgroup = $(evt.target).closest('[data-target="py-home-tab"]');
    tabtarget = $(evt.target).attr("data-target");
    tab = {'tbg':tabgroup,'tbt':tabtarget};
    pytab.opentab(tab);

}

function closeTab(event){
    tabgroup = $(event.target).closest('[data-target="py-home-tab"]');
    tabtarget = $(event.target).closest("button");
    tab = {'tbg':tabgroup, 'tbt':tabtarget};
    pytab.removetab(tab);

}

function addTab(event){
    sampledata = {'tabname':'Sample','tabgroup':'py-home-tab','tabconteent': '<h3>Hello<h3/>'};
    pytab.addtab(event,sampledata);
}

function opencollapse(event){
    parent_row = $(event.target).attr('data-id');
    parent_ele = $(event.target).closest('[data-target="'+parent_row+'"]').attr('data-root');
    parent = $(event.target).closest('[data-parent="'+parent_ele+'"]');
    $(parent.find('[data-type="header"]')).each(function(){
        i = $( this );
        i.removeClass(" collapsibleactive");
    });
    $(parent.find('[data-type="content"]')).each(function(){
        i = $( this );
        i.removeClass(" contentactive");
    });
    $(event.target).closest('[data-target="'+parent_row+'"]').find('[data-id="'+parent_row+'"]').each(function(){
        i = $(this);
        if(i.attr('data-type')=="header"){
            i.addClass(" collapsibleactive");
        }else{
            i.addClass(" contentactive");
        }
    });

}