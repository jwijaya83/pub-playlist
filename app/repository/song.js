const db = require("../models");
const Song = db.song;
const Op = db.Sequelize.Op;

exports.create = (req) => {
    const song = {
        id: req.id,
        title: req.title,
        artist: req.artist,
        album: req.album,
        duration: req.duration
    };

    return Song.create(song);
};

exports.findAll = (req) => {
    const condition = req.ids ? {id: req.ids} : null;
    return Song.findAll({where: condition});
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id);
};
