/*global $, document, alert*/
(function () {
    "use strict";

    function update_todo(todo_id, state, next_transition) {

        var icon,
            icon_url,
            img_src,
            link,
            new_url,
            url_parts;

        // update the state of the text
        $('#' + todo_id + ' td.todo-state').text(state);
        // change the next status url
        link = $('#' + todo_id + ' td.todo-visual-status a');
        new_url = link.attr('href').split("=")[0] + "=" + next_transition;
        link.attr('href', new_url);
        // update the image.
        icon = $('#' + todo_id + ' td.todo-visual-status img');
        icon_url = state + ".png";
        url_parts = icon.attr('src').split('/');
        // remove trailing image. nasty.
        url_parts.splice(url_parts.length - 1);
        img_src = url_parts.join("/") + "/" + icon_url;
        icon.attr('src', img_src);
    }

    $(document).ready(function (e) {
        $("table#todo-summary td.todo-visual-status a").click(function (event) {

            var target,
                url,
                error_msg;

            // stop the browser from submitting after we know all is well
            event.preventDefault();
            target = $(this);
            url = target.attr('href');
            error_msg = "There was an error updating this item - please try again!";
            $.ajax({
                url: url,
                method: 'GET',
                success: function (data) {

                    var state,
                        transition;

                    if (data.success) {
                        state = data.results.state;
                        transition = data.results.transitions[0];
                        update_todo(target.closest('tr').attr('id'), state, transition);
                    } else {
                        // This could be nicer in the future...
                        alert(error_msg + data.messages);
                    }
                },
                error: function (data) {
                    alert(error_msg);
                }
            });

        });
    });


}());