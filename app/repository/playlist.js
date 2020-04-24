const db = require("../models");
const Playlist = db.playlist;
const Op = db.Sequelize.Op;

exports.findAll = () => {
    return Playlist.findAll();
}
