$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('div#hello').empty();
    const len = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('div#hello').append(data.hello);
      }
    });
  });
})
