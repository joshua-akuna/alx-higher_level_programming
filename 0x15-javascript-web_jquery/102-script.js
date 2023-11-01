$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    const input = $('INPUT#language_code').val();
    if (!input) {
      return;
    }
    const URL = 'https://www.fourtonfish.com/hellosalut/hello/?';
    $.get(URL + $.param({ lang: `${input}` }), (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
