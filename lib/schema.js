const { buildSchema } = require('graphql');
const graphqlHTTP = require('express-graphql');
const Songs = require('./songs');
const path = require('path');

let library = new Songs(path.join(__dirname, '..', 'data'));

const schema = buildSchema(`
    type Query {
        library(id: Int): Song,
        libraries: [Song],
        playlist(id: Int!): Playlist,
        playlists: [Playlist]
    }
    type Mutation {
        createPlaylist(name: String!, songs: [Int]): Playlist,
        deletePlaylist(id: Int!): Playlist
    }
    type Song {
        id: Int!,
        album: String!,
        duration: Int!,
        title: String!,
        artist: String!
    }
    type Playlist {
        id: Int!,
        name: String!,
        songs: [Song]
    }
`);

const rootResolver = {
    library: graphqlInput => library.getSong(graphqlInput && graphqlInput.id),
    libraries: library.getLibrary(),
    playlist: graphqlInput => library.getPlaylist(graphqlInput && graphqlInput.id),
    playlists: graphqlInput => library.getPlaylists(() => {}),
    createPlaylist: graphqlInput => {
        let result = null;
        library.savePlaylist(null, graphqlInput.name, graphqlInput.songs, (error, id) => {
            result = {id}
        });
        return result
    },
    deletePlaylist: graphqlInput => {
        library.deletePlaylist(graphqlInput.id);
        return {id: graphqlInput.id}
    }
};

const graphql = graphqlHTTP({
    schema,
    rootValue: rootResolver,
    graphiql: true
})

module.exports = graphql;
