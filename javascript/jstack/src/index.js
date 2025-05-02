const http = require('http');





const server = http.createServer((request, response) => {
  console.log(`Request method: ${request.method} | Endpoint: ${request.url}`);


  const route = route.find((routeObj) => (
    routeObj.endpoint === Request.url && routeObj.method === request.method
  ));

  // if (request.url === '/users' && request.method === 'GET') {
  //   UserController.listUsers(request, response)

  // } else {
  //   response.writeHead(404, { 'Content-type': 'text/html' });
  //   response.end('<h1>Erro 404</h1>')
  // }

  // response.writeHead(200, { 'Content-Type': 'text/html' });
  // response.end('<h1>Hello world!</h1>');
});

server.listen(3000, () => console.log('🥵 Server started at http://localhost:3000'))

