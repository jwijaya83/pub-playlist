const { buildSchema } = require('graphql');
const graphqlHTTP = require('express-graphql');
const playlistRepository = require('../repository/playlist');
const songRepository = require('../repository/song');

const schema = buildSchema(`
    type Query {
        library(id: Int): Song,
        libraries(search: String): [Song],
        playlist(id: Int!): Playlist,
        playlists: [Playlist]
    }
    type Mutation {
        createPlaylist(name: String!, songs: [Int]): PlaylistResponse,
        editPlaylist(id: Int!, name: String, songs: [Int]): PlaylistResponse,
        deletePlaylist(id: Int!): PlaylistResponse
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
    type PlaylistResponse {
        id: Int!
    }
`);

const rootResolver = {
    library: async req => await songRepository.findOne({id: req && req.id}),
    libraries: async req => await songRepository.findAll(req && {search: req.search}),
    playlist: async req => await playlistRepository.findOne({id: req && req.id}),
    playlists: async () => await playlistRepository.findAll(),
    createPlaylist: async req => await playlistRepository.create(req && {name: req.name, songs: req.songs}),
    editPlaylist: async req => await playlistRepository.edit(req && {id: req.id, name: req.name, songs: req.songs}),
    deletePlaylist: async req => await playlistRepository.delete(req && {id: req.id})
};

const graphql = graphqlHTTP({
    schema,
    rootValue: rootResolver,
    graphiql: true
});

module.exports = graphql;
