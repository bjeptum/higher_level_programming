//Updates the text of the header element when the user clicks on
$(document).ready(function() {
    $("#update_header").click(function() {
        $('header').text('New Header!!!');
    });
  });