const express = require('express');
const schema = require('./app/controller/schema.js');
const Import = require('./app/service/import').Import;

let port = 3000;
const app = express();
app.use('/', schema);

const db = require("./app/models");
// db.sequelize.sync();
db.sequelize.sync({ force: true }).then(() => {
    console.log("Drop and re-sync db.");
    Import.toDB();
    console.log("Data library imported.");
});

app.listen(port);
console.log('GraphQL API server running at localhost:'+ port);
