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

exports.findAll = (req) => {
    const condition = req.ids ? {id: req.ids} : null;
    return Song.findAll({where: condition});
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id);
};

exports.findAllTr = async (req, t) => {
    const condition = req.ids ? {id: req.ids} : null;
    return await Song.findAll({
        where: condition,
        transaction: t
    });
};
