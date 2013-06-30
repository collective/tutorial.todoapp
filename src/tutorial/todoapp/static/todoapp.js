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

            var ajax_url,
                error_msg,
                template_url,
                $target;

            error_msg = "There was an error updating this item - please try again!";

            // stop the browser from submitting after we know all is well
            event.preventDefault();

            // Build AJAX URL - we need to change URL from the template:
            //     http://localhost:8080/Plone/todo/get-milk/content_status_modify?workflow_action=<transition_id>
            // to URL for AJAX call:
            //     http://localhost:8080/Plone/todo/get-milk/update_workflow?transition=<transition_id>
            $target = $(this);
            template_url = $target.attr("href");
            ajax_url = template_url.replace("content_status_modify?workflow_action", "update_workflow?transition");

            $.ajax({
                url: ajax_url,
                method: "GET",
                success: function (data) {

                    var state,
                        transition;

                    if (data.success) {
                        state = data.results.state;
                        transition = data.results.transitions[0];
                        update_todo($target.closest("tr").attr("id"), state, transition);
                    } else {
                        // This could be nicer in the future...
                        alert(error_msg + "\n\nError:\n" + data.messages);
                    }
                },
                error: function (data) {
                    alert(error_msg);
                }
            });

        });
    });


}());