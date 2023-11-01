$('document').ready(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
});
