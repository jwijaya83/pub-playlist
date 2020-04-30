const dbConfig = require("../config/db");
const Sequelize = require("sequelize");

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

// Many-to-many association with a join table.
db.playlist.belongsToMany(db.song, {as: 'songs', through: 'songs_in_playlist', foreignKey: 'playlist_id', otherKey: 'song_id'});
db.song.belongsToMany(db.playlist, {as: 'playlists', through: 'songs_in_playlist', foreignKey: 'song_id', otherKey: 'playlist_id'});

module.exports = db;
