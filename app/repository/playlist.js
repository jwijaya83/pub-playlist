const db = require("../models");
const Playlist = db.playlist;
const Song = db.song;
const SongRepository = require('./song');

const _setSongs = async (req, t) => {
    let songs = [];
    if (req.songs !== undefined) {
        songs = await SongRepository.findAll({ids: req.songs}, t);
    }
    await req.playlist.setSongs(songs, {transaction: t});
    return {id: req.playlist.id}
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
        throw error;
    }
};

exports.edit = async (req) => {
    const conditions = {
        name: req.name
    };
    try {
        return await db.Sequelize.transaction(async (t) => {
            let result = await Playlist.update(conditions, {where: {id: req.id}, transaction: t});
            if (result.length > 0) {
                let playlist = await Playlist.findOne({where: {id: req.id}, transaction: t});
                return _setSongs({...req, playlist}, t);
            } else {
                throw new Error("Play list with id " + req.id + " has not been found");
            }
        });
    } catch (error) {
        console.error(error);
        throw error;
    }
};

exports.delete = (req) => {
    return Playlist.destroy({
        where: {
            id: req.id
        }
    }).then(data => {
        if (data > 0) {
            console.log("Playlist id=" + req.id + " has been deleted");
        }
        return {id: req.id}
    });
};

const _conditionManyToMany = {
    include: [{
        model: Song,
        as: 'songs',
        through: {
            attributes: ['playlist_id', 'song_id']
        }
    }]
};

exports.findOne = (req) => {
    const id = req.id;
    return Playlist.findByPk(id, _conditionManyToMany);
};

exports.findAll = () => {
    return Playlist.findAll(_conditionManyToMany);
};
