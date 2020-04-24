module.exports = (sequelize, Sequelize) => {
    const Song = sequelize.define("song", {
        album: {
            type: Sequelize.STRING,
            allowNull: false
        },
        duration: {
            type: Sequelize.INTEGER,
            allowNull: false
        },
        title: {
            type: Sequelize.STRING,
            allowNull: false
        },
        artist: {
            type: Sequelize.STRING,
            allowNull: false,
        }
    });

    return Song;
};
