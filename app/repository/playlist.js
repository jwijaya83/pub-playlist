const db = require("../models");
const Playlist = db.playlist;
const Song = db.song;
const SongRepository = require('./song');
const Op = db.Sequelize.Op;

const _setSongs = (req) => {
    if (req.songs !== undefined) {
        SongRepository.findAll({
            ids: req.songs
        }).then(songs => {
            req.playlist.setSongs(songs);
        });
    }
};

exports.create = (req) => {
    const conditions = {
        id: req.id,
        name: req.name
    };
    //TODO: need to add transaction
    return Playlist.create(conditions)
        .then(playlist => {
            _setSongs({...req, playlist});
            return {id: playlist.id}
        });
};

exports.edit = (req) => {
    const conditions = {
        name: req.name
    };
    //TODO: need to add transaction
    return Playlist.update(conditions, {where: {id: req.id}})
        .then(data => {
            return exports.findOne({id: req.id});
        }).then(playlist => {
            _setSongs({...req, playlist});
            return {id: playlist.id};
        });
};

exports.delete = (req) => {
    return Playlist.destroy({
        where: {
            id: req.id
        }
    }).then(data => {return {id: req.id}});
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
