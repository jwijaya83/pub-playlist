const express = require('express');
const schema = require('./app/controller/schema.js');
const Import = require('./app/service/import').Import;
const cors = require("cors");

let port = 3000;
const app = express();
const allowedOrigins = [
    'http://localhost:3000',
    'http://localhost:4000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:4000'
];
app.use(cors({
    origin: function(origin, callback){
        if (!origin) return callback(null, true);
        if (allowedOrigins.indexOf(origin) === -1) {
            const msg = 'The CORS policy for this site does not allow access from the specified Origin.';
            return callback(new Error(msg), false);
        }
        return callback(null, true);
    }

}));
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
