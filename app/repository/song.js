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

const _searchCondition = (search) => {
    let criteriaLeft = search;
    let criteriaAddition = {};
    if (search.indexOf("?") >= 0) {
        let criteria = search.split("?");
        criteriaLeft = criteria[0];
        let criteriaRight = criteria[1];
        if (criteriaRight.length >= 2) {
            switch (criteriaRight[0]) {
                case ">":
                    criteriaAddition = {duration:{[Op.gt]: parseInt(criteriaRight.substring(1))}};
                    break;
                case "<":
                    criteriaAddition = {duration:{[Op.lt]: parseInt(criteriaRight.substring(1))}};
                    break;
            }
        }
    }
    return  {...criteriaAddition,
        [Op.or]: {
            title: { [Op.iLike]: `%${criteriaLeft}%` },
            artist: { [Op.iLike]: `%${criteriaLeft}%` },
            album: { [Op.iLike]: `%${criteriaLeft}%` }
        }
    };
};

exports.findAll = (req, t) => {
    let condition = req.ids ? {id: req.ids} : null;
    condition = req.search ? _searchCondition(req.search) : condition;

    return Song.findAll({
        where: condition,
        transaction: t
    });
};

exports.findOne = (req) => {
    const id = req.id;
    return Song.findByPk(id);
};

