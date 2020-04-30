# Playlistify

> Web application for creating playlists from a library of songs.
> The next level playlist experience!

## How to install and start the web application

#### Server

Run Postgres and create `playlist` DB using a Docker command.

```bash
docker run -d --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=playlist -p "5432:5432" postgres
```

Run `pgAdmin` - a management tool for PostgreSQL.
```bash
docker run -d --name pgadmin4 -e PGADMIN_DEFAULT_EMAIL=pgadmin4 -e PGADMIN_DEFAULT_PASSWORD=pgadmin4 -p "8880:80" dpage/pgadmin4
```
Install dependencies and start server:
```bash
npm install
npm run start:server
```
Served at http://localhost:3000/

#### UI

Install dependencies, build UI and start dev server:
```bash
npm install
npm run build:ui
npm run start:ui
```
Served at http://localhost:4000/

#### Automated tests
Install Python v3.7.*  
Download Chrome Driver from https://chromedriver.chromium.org/downloads  
Extract Chrome Driver from archive to and folder from PATH variable  
Install dependencies:  
```bash 
pip install -r requirements.txt
```  
Run Server and WebUI as described in sections above.  

Run tests from `tests\` directory.   
- _For running all tests:_  
```bash
pytest
```  
- _For running specific tests:_  
```bash
pytest <tests_filename>.py  
```

## Features

##### Frontend:
1. Load the library of songs and show it in the browser. 
2. Add songs from the library to a playlist. 
3. Name and save a playlist.
4. List saved playlists. 
5. Load saved playlists.
6. Search/filtering for a particular entry/song criteria.  
 _Search details:_
 `someName?>240` - means search `someName` in artist/album/song names and song duration should be more than 240).
 The result will be returned via the backend GraphQL API.

##### Backend:
1. GraphQL API.
2. GraphQL query, mutation, resolver.
3. PostgeSQl as a data source.
4. Sequelize ORM (transactions support)
5. Mocha test framework

_**To be done**_    
DB constraints.  
Server-side Batching & Caching via DataLoader.   
Pagination.  
Add auto downloading Browser drivers for UI tests.

## DB Schema
```sql
CREATE TABLE public.playlists (
	id serial NOT NULL,
	name varchar(255) NULL,
	"createdAt" timestamptz NOT NULL,
	"updatedAt" timestamptz NOT NULL,
	CONSTRAINT playlists_pkey null
);
CREATE TABLE public.songs (
	id serial NOT NULL,
	album varchar(255) NOT NULL,
	duration int4 NOT NULL,
	title varchar(255) NOT NULL,
	artist varchar(255) NOT NULL,
	"createdAt" timestamptz NOT NULL,
	"updatedAt" timestamptz NOT NULL,
	CONSTRAINT songs_pkey null
);
CREATE TABLE public.songs_in_playlist (
	"createdAt" timestamptz NOT NULL,
	"updatedAt" timestamptz NOT NULL,
	playlist_id int4 NOT NULL,
	song_id int4 NOT NULL,
	CONSTRAINT songs_in_playlist_pkey null,
	CONSTRAINT songs_in_playlist_playlist_id_fkey null,
	CONSTRAINT songs_in_playlist_song_id_fkey null
);
```

## API

GraphQL API schema.
```js
type Query {
    library(id: Int): Song,
    libraries: [Song],
    playlist(id: Int!): Playlist,
    playlists: [Playlist]
}
type Mutation {
    createPlaylist(name: String!, songs: [Int]): PlaylistResponse,
    editPlaylist(id: Int!, name: String, songs: [Int]): PlaylistResponse,
    deletePlaylist(id: Int!): PlaylistResponse
}
```
#### GraphQL API methods:

_**GET libraries**_  
```js
query {
  libraries {
    id,
    title,
    duration,
    artist
  }
}

Returns a JSON array of songs.
{
  "data": {
    "libraries": [
      {
        "id": 617,
        "title": "My Paper Heart",
        "duration": 228,
        "artist": "The All-American Rejects"
      },
      {
        "id": 1,
        "title": "Your Star",
        "duration": 260,
        "artist": "The All-American Rejects"
      }
      ...
    ]
}
```

_**GET library by id**_

```js
query {
  library(id: 1) {
    id,
    title,
    artist,
    duration,
    album
  }
}

Returns a JSON object for a song with given `id`.
{
  "data": {
    "library": {
      "id": 1,
      "title": "Your Star",
      "artist": "The All-American Rejects",
      "duration": 260,
      "album": "The All-American Rejects"
    }
  }
}
```

_**GET playlists**_
```js
query {
  playlists {
    id,
    songs {
      id,
      duration,
      album,
      artist
    }
  }
}

Returns a JSON array of playlists.
{
  "data": {
    "playlists": [
      {
        "id": 1,
        "songs": [
          {
            "id": 617,
            "duration": 228,
            "album": "The All-American Rejects",
            "artist": "The All-American Rejects"
          },
          {
            "id": 1,
            "duration": 260,
            "album": "The All-American Rejects",
            "artist": "The All-American Rejects"
          }
          ...
        ]
      }
      ...
    ]
  }
```

_**GET playlist by id**_

```js
query {
  playlist(id: 1) {
    id,
    name,
    songs {
      id,
      artist,
      duration,
      title
    }
  }
}

Returns a JSON object with the playlist with given `id`.
{
  "data": {
    "playlist": {
      "id": 1,
      "name": "Ryan's Megamix",
      "songs": [
        {
          "id": 617,
          "artist": "The All-American Rejects",
          "duration": 228,
          "title": "My Paper Heart"
        }
        ...
      ]
    }
  }
```

_**POST create playlist**_
```js
mutation {
  createPlaylist(name: "My New Playlist", 
    songs:  
    [1,2, 1000]
  ) {
    id
  }
}

Returns created playlis id.
{
  "data": {
    "createPlaylist": {
      "id": 9
    }
  }
}
```

_**POST edit playlist**_
```js
mutation {
  editPlaylist(id: 9, name: "My New Playlist Updated", 
    songs:  
    [3,4]
  ) {
    id
  }
}

Returns updated playlis id.
{
  "data": {
    "createPlaylist": {
      "id": 9
    }
  }
}
```

_**POST delete playlist**_
```js
mutation {
  deletePlaylist(id: 9) {
    id
  }
}

Returns deleted playlist id
{
  "data": {
    "deletePlaylist": {
      "id": 9
    }
  }
}
```

_**GET search in library**_
```js
query {
  libraries (search: "Time Stands Still") {
    id,
    title,
    duration,
    artist
  }
}

Returns search result.
{
  "data": {
    "libraries": [
      {
        "id": 3,
        "title": "Time Stands Still",
        "duration": 210,
        "artist": "The All-American Rejects"
      }
    ]
  }
}
```

_**Error response example**_
```js
mutation {
  editPlaylist(id: 999, name: "My New Playlist Updated", 
    songs:  
    [3,4]
  ) {
    id
  }
}

Error response.
{
  "errors": [
    {
      "message": "Play list with id 999 has not been found",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "editPlaylist"
      ]
    }
  ],
  "data": {
    "editPlaylist": null
  }
}
```