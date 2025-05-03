const cheerio = require('cheerio');

const PAGINA_HTML = `<html>
<head>
  <title>Lista de aprovados</title>
</head>
<body>
<ul id="nomes">
  <li class="primeiro">Pedro</li>
  <li class="segundo"Fernanda</li>
  <li class="terceiro">João</li>
</ul>

</body>
</html>
`

const $ = cheerio.load(PAGINA_HTML)
// const DADOS = $('*').text();
// const DADOS = $('#nomes').text();
// const DADOS = $('.primeiro').text();
// const DADOS = $('.primeiro', '#nomes').text();

console.log(DADOS)