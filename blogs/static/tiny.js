var script  = document.createElement('script')
script.type = 'text/javascript'
script.src = 'https://cdn.tiny.cloud/1/1gfz6afqmfj1ng50cjlpdqjyrlp0onnwmecz80n0m9sty0a2/tinymce/6/tinymce.min.js'
document.head.appendChild(script)
script.onload = function(){
tinymce.init({
    selector: '#id_content',
    width: 960,
    height: 700,
    plugins: [
      'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
      'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
      'media', 'table', 'emoticons', 'template', 'help'
    ],
    toolbar: 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
      'forecolor backcolor emoticons | help',
    menu: {
      favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
    },
    menubar: 'favs file edit view insert format tools table help',
    content_css: 'css/content.css'
  });}


