const axios = require('axios');
const cheerio = require('cheerio')

//https://www.gov.br/mds/pt-br/noticias-e-conteudos/noticias
axios.get('https://www.gov.br/mds/pt-br/noticias-e-conteudos/noticias')
  .then(resp => {
    let dadoshtml = resp.data;
    const $ = cheerio.load(dadoshtml);

    noticias = []
    $('a.summary.url')
      .each((_, e) => {
        const titulo = $(e).text().trim();
        const link = $(e).attr('href');
        noticias.push({ titulo, link })

      });
    console.log(noticias);
  })


