const axios = require('axios');

axios.get('http://www2.aneel.gov.br/scg/gd/GD_Fonte.asp').then(resp => {
  // console.log(resp.statusText);
  // console.log(resp.statusText);
  // console.log(resp.headers);
  // console.log(resp.config)
  console.log(resp.data);
})