//Adds a <li> element to a list when the user clicks on the tag
$(document).ready(function() {
  $("#add_item").click(function() {
    var newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});
