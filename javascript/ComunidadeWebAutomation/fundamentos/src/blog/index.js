const axios = require('axios');
const cheerio = require('cheerio')

//https://www.gov.br/pagina-interna-noticias-ebc

axios.get('https://www.gov.br/pagina-interna-noticias-ebc')
  .then(resp => {
    let dadoshtml = resp.data;
    const $ = cheerio.load(dadoshtml)

  })
