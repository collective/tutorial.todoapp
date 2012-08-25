/*global $, document*/
(function () {
    "use strict";

    function update_todo(todo_id, state, next_transition){
        // TODO: use css instead of replacing images

        // update the state of the text
        $('#'+todo_id+' td.todo-state').text(state);
        // change the next status url
        var link = $('#'+todo_id+' td.todo-visual-status a');
        var new_url = link.attr('href').split("=")[0] + "=" + next_transition;
        link.attr('href', new_url); 
        // update the image. 
        var icon = $('#'+todo_id+' td.todo-visual-status img');
        var icon_url = state + ".png";
        var url_parts = icon.attr('src').split('/');
        // remove trailing image. nasty.
        url_parts.splice(url_parts.length-1)
        var img_src = url_parts.join("/") + "/" + icon_url; 
        icon.attr('src', img_src);
    }
    
    $(document).ready(function(e){
        $("table#todo-summary td.todo-visual-status a").click(function(event){
            // stop the browser from submitting after we know all is well
            event.preventDefault();
            var target = $(this);
            var url = target.attr('href');
            var error_msg = "There was an error updating this item - please try again!"
            $.ajax({
                url: url,
                method: 'GET',
                success: function(data){
                    if (data.success){
                        var state = data.results.state;
                        var transition = data.results.transitions[0];
                        update_todo(target.closest('tr').attr('id'), state, transition);
                    } else {
                        // This could be nicer in the future... 
                        alert(error_msg + data.messages);
                    }
                },
                error: function(data){
                    alert(error_msg);
                }
            });

        });
    });


}());