const path = require('path');
const song = require('../repository/song');
const playlist = require('../repository/playlist');
const fs = require('fs');

class Songs {
   constructor(dataPath) {
      this._dataPath = dataPath;
   }

   _loadLibrary = () => {
      if (this._library) {
         return this._library;
      }

      const pathname = path.join(this._dataPath, "library.json");
      const input = fs.readFileSync(pathname);

      this._library = JSON.parse(input);

      return this._library;
   };

   getLibrary = () => {
      this._loadLibrary();

      return this._library;
   }

   getPlaylists = () => {
      const pathname = path.join(this._dataPath, "playlists");

      let files = fs.readdirSync(pathname);

      files = files.filter(function(item) {
         return !/^\./.test(item);
      }).map(function(item) {
         return path.join(pathname, item);
      });

      let playlists = [];
      files.forEach(pathname => {
         playlists.push(JSON.parse(fs.readFileSync(pathname)));
      });
      return playlists;
   };

   toDB = async () => {
      const data = this.getLibrary();
      await data.forEach(item => {
         song.create(item);
      })

      const playlists = this.getPlaylists();
      playlists.forEach(item => {
         if (item !== undefined) {
            playlist.create(item);
         }
      });
   }
}

const songs = new Songs(path.join(__dirname, '..', '..', 'data'));
songs.toDB();
