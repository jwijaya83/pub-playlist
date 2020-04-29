const db = require("../models");
const Song = db.song;
const Op = require("sequelize").Op;

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

exports.findAll = (req, t) => {
    let condition = req.ids ? {id: req.ids} : null;
    condition = req.search ? {
        [Op.or]: {
            title: {[Op.iLike]: `%${req.search}%`},
            artist: {[Op.iLike]: `%${req.search}%`},
            album: {[Op.iLike]: `%${req.search}%`}
        }
    } : condition;

    return Song.findAll({
        where: condition,
        transaction: t
    });
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id);
};

