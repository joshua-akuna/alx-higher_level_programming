$('document').ready(() => {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(URL, (data, textStatus) => {
    for (const movie of data.results) {
      const newItem = document.createElement('li');
      newItem.innerHTML = movie.title;
      $('UL#list_movies').append(newItem);
    }
  });
});
