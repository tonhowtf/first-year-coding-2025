const axios = require('axios');
const cheerio = require('cheerio')

// https://pedroalpacheco.github.io/htmlpurocurso/

axios.get('https://pedroalpacheco.github.io/htmlpurocurso/')
  .then(resp => {
    let dadoshtml = resp.data;
    const $ = cheerio.load(dadoshtml)
    // const tudo = $('.col-4').html()
    // const otitulo = $('h1').text();
    // const verificaclasse = $('a').hasClass('text-muted')
    // const destaque = $('[]')
    const meses = $('[class="list-unstyled mb-0"]').text()
    console.log(meses);
  })