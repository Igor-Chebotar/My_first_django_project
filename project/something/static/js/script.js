// функция, которая копирует короткую ссылку в буфер обмена пользователя
function CopyURL(id) {
  var text = document.getElementById('url_hash_' + id)
  text.select();
  document.execCommand('copy')
}
