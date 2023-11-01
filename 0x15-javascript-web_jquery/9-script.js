$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
