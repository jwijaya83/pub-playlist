const db = require("../models");
const Song = db.song;

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

exports.findAll = async (req, t) => {
    return await Song.findAll({
        where: {id: req.ids},
        transaction: t
    });
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id);
};

