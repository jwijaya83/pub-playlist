import {matchers} from 'jest-json-schema';

const tester = require('graphql-tester').tester;
const config = {
    APP_HOST: "http://localhost",
    APP_PORT: 3000,
    GQL_URL_DIR: "/",
    TEST_TIMEOUT: 30000
};

expect.extend(matchers);


// TODO: Before the test suite run the server first

describe('Playlist API test', function () {
    const self = this;
    self.test = tester({
        url: `${config.APP_HOST}:${config.APP_PORT}/${config.GQL_URL_DIR}`,
        contentType: 'application/json'
    });

    beforeAll(() =>{
        console.log("\x1B[31mPlease make sure server is running on " + config.APP_PORT + " port\x1B[0m");
    });

    // Songs Api
    test('query "libraries", should return all songs', done => {
        const schema = {
            properties: {
                libraries: {
                    type: "array",
                    items: [
                        {
                            type: "object",
                            properties: {
                                id: {
                                    type: "integer"
                                },
                                title: {
                                    type: "string"
                                },
                                duration: {
                                    type: "integer"
                                },
                                artist: {
                                    type: "string"
                                }
                            },
                            required: [
                                "id",
                                "title",
                                "duration",
                                "artist"
                            ]
                        }
                    ]
                }
            },
            required: [
                "libraries"
            ]
        };

        self
            .test(
                JSON.stringify({
                    query: `query {
                                libraries {
                                    id,
                                    title,
                                    duration,
                                    artist
                                }
                            }`,
                }),
                {jar: true} // using my fork shalkam/graphql-tester to be able to add this option to the node request
            )
            .then(res => {
                self.libraries = res.data.libraries;
                expect(res.status).toBe(200);
                expect(res.success).toBe(true);
                expect(self.libraries.length).toBeGreaterThan(0);
                expect(res.data).toMatchSchema(schema);
                done();
            })
            .catch(err => {
                expect(err).toBe(null);
                done();
            });
    });

    // Play lists Api
    test('query "playlists", should return all play lists', done => {
        const schema = {
            properties: {
                playlists: {
                    type: "array",
                    items: [
                        {
                            type: "object",
                            properties: {
                                id: {
                                    type: "integer"
                                },
                                songs: {
                                    type: "array",
                                    items: [
                                        {
                                            type: "object",
                                            properties: {
                                                id: {
                                                    type: "integer"
                                                },
                                                duration: {
                                                    type: "integer"
                                                },
                                                album: {
                                                    type: "string"
                                                },
                                                artist: {
                                                    type: "string"
                                                }
                                            },
                                            required: [
                                                "id",
                                                "duration",
                                                "album",
                                                "artist"
                                            ]
                                        }
                                    ]
                                }
                            },
                            required: [
                                "id",
                            ]
                        }
                    ]
                }
            },
            required: [
                "playlists"
            ]
        };

        self
            .test(
                JSON.stringify({
                    query: `query {
                                playlists {
                                    id,
                                    songs {
                                       id,
                                       duration,
                                       album,
                                       artist
                                    }
                                }
                          }`,
                }),
                {jar: true} // using my fork shalkam/graphql-tester to be able to add this option to the node request
            )
            .then(res => {
                self.playlists = res.data.playlists;
                expect(res.status).toBe(200);
                expect(res.success).toBe(true);
                expect(self.playlists.length).toBeGreaterThan(0);
                expect(res.data).toMatchSchema(schema);
                done();
            })
            .catch(err => {
                expect(err).toBe(null);
                done();
            });
    });
});
