
$(document).ready(function(){
    // Load the header when the head of the page loads.
    $("#hparent").load(
        "header.html",
        function() {
            // Once the header's loaded, make the content visible. Otherwise,
            // the motion's jerky.
            $("#content").css("visibility", "visible");
        }
    );
});
