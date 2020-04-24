module.exports = (sequelize, Sequelize) => {
    const Playlist = sequelize.define("playlist", {
        name: {
            type: Sequelize.STRING
        }
    });

    return Playlist;
};
