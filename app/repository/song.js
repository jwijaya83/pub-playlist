const db = require("../models");
const Song = db.song;
const Op = db.Sequelize.Op;

exports.create = (req) => {
    const song = {
        title: req.title,
        artist: req.artist,
        album: req.album,
        duration: req.duration
    };

    return Song.create(song)
};

exports.findAll = () => {
    return Song.findAll()
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id)
};
