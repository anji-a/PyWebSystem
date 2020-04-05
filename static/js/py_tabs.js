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


function w3tabclick(event){
    tabtargetid = $(event.target).attr('data-tabid');
    tabgroup = $(event.target).closest('[data-target="py-home-tab"]');
    //tabtarget = tabgroup.find('[data-target="tabcontent"]');
    //tablinks = tabgroup.find('[data-target="tablinks"]');
    tablinks = tabgroup.find('[data-linkid="'+tabtargetid+'"]');
    tabtarget = tabgroup.find('[data-contentid="'+tabtargetid+'"]');
    tabid = $(event.target).attr('data-target');
    $(tablinks.find('[data-tabid="'+tabtargetid+'"]')).each(function(){
        i = $( this );
        console.log(i);
        i.removeClass(" active");
        if (i.attr('data-target')==tabid){
            i.addClass(" active");
        }
    });
    $(tabtarget.find('[data-tabid="'+tabtargetid+'"]')).each(function(){
        i = $( this );
        console.log(i);
        i.removeClass(" display");
        if (i.attr('data-target')==tabid){
            i.addClass(" display");
        }
    });
}

function w3openworktab(event, tabname, tabcontent ){
    tabavilable = false;
    worktab = $(document).find('[data-worktab="true"]')[0];
    tabid = $($(worktab).find('[data-target="tablinks"]')[0]).attr("data-linkid");
    tablinks = $(worktab).find('[data-linkid="'+tabid+'"]');
    $(tablinks.find('[data-tabid="'+tabid+'"]')).each(function(){
        console.log($(this), this.textContent);
        if( this.textContent.includes(tabname)){
            tabavilable = true;
            contentid = $(this).attr('data-target');
        }
    });
    if(tabavilable== false){
        tabcontentid = pw().generateid(10);
        tablink = '<button class="w3-bar-item w3-button tablink" data-tabid="'+tabid+'" data-type="TabLink"  data-target="'+tabcontentid+'" onclick="w3tabclick(event)">'+tabname+'<span class="tabclose" onclick="processeventaction(event)" data-controlset=\'{"actionset":[{"event":"click", "eventdata":[{"action":"closeTab"}]}]}\'>X</span></button>';
        tabcontent ='<div data-target="'+tabcontentid+'" data-tabid="'+tabid+'" data-type="TabData" class="nodisplay">'+tabcontent+'</div>';
        $(worktab).find('[data-linkid="'+tabid+'"]').append(tablink);
        $(worktab).find('[data-contentid="'+tabid+'"]').append(tabcontent);
        w3activateworkTab(worktab, tabid, tabcontentid);
    }else{
        //tabcontent ='<div data-target="'+tabcontentid+'" data-tabid="'+tabid+'" data-type="TabData" class="nodisplay">'+tabcontent+'</div>';
        $(worktab).find('[data-contentid="'+tabid+'"]').find('[data-target="'+contentid+'"]').html(tabcontent);
        w3activateworkTab(worktab, tabid, tabcontentid);
    }
    console.log(worktab);
}

function w3activateworkTab(worktabs,tabid, contentid){
    tablinks = $(worktabs).find('[data-linkid="'+tabid+'"]');
    tabtarget = $(worktabs).find('[data-contentid="'+tabid+'"]');
    $(tablinks.find('[data-tabid="'+tabid+'"]')).each(function(){
        i = $( this );
        //console.log(i);
        i.removeClass(" active");
        if (i.attr('data-target')==contentid){
            i.addClass(" active");
        }
    });
    $(tabtarget.find('[data-tabid="'+tabid+'"]')).each(function(){
        i = $( this );
        //console.log(i);
        i.removeClass(" display");
        if (i.attr('data-target')==contentid){
            i.addClass(" display");
        }
    });
}

function getWorkTabData(event){
    tabdetails = {}
    tabcontentid = $(event.target).closest('[data-type="TabLink"]').attr("data-target");
    tabid = $(event.target).closest('[data-type="TabLink"]').attr("data-tabid");
    worktab = $(event.target).closest('[data-worktab="true"]')[0];
    tabcontent = $(worktab).find('[data-contentid="'+tabid+'"]');
    tabdetails.tabid = tabid;
    tabdetails.tabcontentid = tabcontentid;
    $(tabcontent.find('[data-tabid="'+tabid+'"]')).each(function(){
        i = $( this );
        if (i.attr('data-target')==tabcontentid){
            worknode = i.find('[data-find="worknode"]').attr("data-node");
            tabdetails.worknode = worknode;
        }
    });
    return tabdetails;
}

function w3closeworktab(event, tabid, tabcontentid){
    worktab = $(event.target).closest('[data-worktab="true"]')[0];
    tablinks = $(worktab).find('[data-linkid="'+tabid+'"]');
    tabtarget = $(worktab).find('[data-contentid="'+tabid+'"]');
    $(tablinks.find('[data-tabid="'+tabid+'"]')).each(function(){
        i = $( this );
        if (i.attr('data-target')==tabcontentid){
            i.remove();
            return false;
        }
    });
    $(tabtarget.find('[data-tabid="'+tabid+'"]')).each(function(){
        i = $( this );
        if (i.attr('data-target')==tabcontentid){
            i.remove();
            return false;
        }else{
            contentid = i.attr('data-target')
        }
    });
    w3activateworkTab(worktab, tabid, contentid);
}

