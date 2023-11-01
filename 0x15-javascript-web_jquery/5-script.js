$('document').ready(() => {
  $('DIV#add_item').click(() => {
    const newItem = document.createElement('li');
    newItem.innerHTML = 'Item';
    $('UL.my_list').append(newItem);
  });
});
