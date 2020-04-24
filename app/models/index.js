const dbConfig = require("../config/db");
const Sequelize = require("sequelize")

const sequelize = new Sequelize(dbConfig.DB, dbConfig.USER, dbConfig.PASSWORD, {
    host: dbConfig.HOST,
    port: dbConfig.PORT,
    dialect: dbConfig.dialect,
    operatorsAliases: false
});

const db = {};

db.Sequelize = sequelize;
db.sequelize = sequelize;
db.playlist = require("./playlist")(sequelize, Sequelize);
db.song = require("./song")(sequelize, Sequelize);

module.exports = db;
