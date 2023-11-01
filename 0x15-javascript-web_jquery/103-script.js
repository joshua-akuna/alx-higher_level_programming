$('document').ready(() => {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keyup((e) => {
    if (e.keyCode === 13) {
      translated();
    }
  });
});

const translate = () => {
  const input = $('INPUT#language_code').val();
  if (!input) {
    return;
  }
  const URL = `https://www.fourtonfish.com/hellosalut/hello/?lang=${input}`;
  $.getJSON(URL, (data) => {
    $('#hello').text(data.hello);
  });
};

const translated = () => {
  const input = $('INPUT#language_code').val();
  if (!input) {
    return;
  }
  const URL = `https://www.fourtonfish.com/hellosalut/hello/?lang=${input}`;
  $.ajax({
    url: URL,
    method: 'GET',
    data: `${input}`,
    crossDomain: true,
    success: (data) => {
      $('#hello').text(data.hello);
    }
  });
};
