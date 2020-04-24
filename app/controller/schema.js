const { buildSchema } = require('graphql');
const graphqlHTTP = require('express-graphql');
const path = require('path');
const playlistRepository = require('../repository/playlist');
const songRepository = require('../repository/song');

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
    library: async graphqlInput => await songRepository.findOne({id: graphqlInput && graphqlInput.id}),
    libraries: async () => await songRepository.findAll(),
    playlist: async graphqlInput => await playlistRepository.findOne({id: graphqlInput && graphqlInput.id}),
    playlists: async () => await playlistRepository.findAll(),
    createPlaylist: graphqlInput => {},
    deletePlaylist: graphqlInput => {[]
    }
};

const graphql = graphqlHTTP({
    schema,
    rootValue: rootResolver,
    graphiql: true
})

module.exports = graphql;
