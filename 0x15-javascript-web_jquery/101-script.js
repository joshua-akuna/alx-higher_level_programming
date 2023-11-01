$('document').ready(() => {
  // $('header').css('color', '#FF0000');
  // Adds a new list item with text Item to the unordered list
  // when the user clicks 'Add item'
  $('DIV#add_item').click(() => {
    const newItem = document.createElement('li');
    newItem.innerHTML = 'Item';
    $('UL.my_list').append(newItem);
  });

  // Removes the last child item of the unordered list
  // when the user clicks 'Remove item'
  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last-child').remove();
  });

  // All elements of the list are removed when the user
  // clicks on 'Clear list'
  $('DIV#clear_list').click(() => {
    // $('header').css('color', 'red');
    $('UL.my_list').empty();
  });
});
