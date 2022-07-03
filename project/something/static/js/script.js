
function CopyURL() {
  var text = document.getElementById('url_hash')
  text.select();
  document.execCommand('copy')
}
