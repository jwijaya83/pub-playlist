const db = require("../models");
const Playlist = db.playlist;
const Song = db.song;

const _setSongs = async (req, t) => {
    if (req.songs !== undefined) {
        let songs = await Song.findAll({
            where: {
                id: req.songs
            },
            transaction: t
        });
        await req.playlist.setSongs(songs, {transaction: t});
        return {id: req.playlist.id}
    }
};

exports.create = async (req) => {
    const conditions = {
        name: req.name
    };
    try {
        return await db.Sequelize.transaction(async (t) => {
            let playlist = await Playlist.create(conditions, {transaction: t});
            return _setSongs({...req, playlist}, t);
        });
    } catch (error) {
        console.error(error);
    }
};

exports.edit = async (req) => {
    const conditions = {
        name: req.name
    };
    try {
        return await db.Sequelize.transaction(async (t) => {
            let result = await Playlist.update(conditions, {where: {id: req.id}, transaction: t});
            if (result[0] > 0) {
                let playlist = await Playlist.findOne({where: {id: req.id}, transaction: t});
                return _setSongs({...req, playlist}, t);
            } else {
                throw new Error("Play list with id " + req.id + " has not been found");
            }
        });
    } catch (error) {
        console.error(error);
    }
};

exports.delete = (req) => {
    return Playlist.destroy({
        where: {
            id: req.id
        }
    }).then(data => {
        return {id: req.id}
    });
};

