$('document').ready(() => {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(URL, (data, textStatus) => {
    $('DIV#hello').text(data.hello);
    // console.log(data.hello);
  });
});
