$('document').ready(() => {
  const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(URL, (data, textStatus) => {
    $('DIV#character').text(data.name);
  });
});
