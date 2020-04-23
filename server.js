const express = require('express');
const schema = require('./lib/schema.js');

let port = 3000;
const app = express();
app.use('/', schema);

app.listen(port);
console.log('GraphQL API server running at localhost:'+ port);
