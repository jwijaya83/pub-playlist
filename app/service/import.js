const path = require('path');
const song = require('../repository/song');
const playlist = require('../repository/playlist');
const fs = require('fs');
const fetch = require('node-fetch');
const convert = require('xml-js');
const https = require('https');

class Import {
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

   // Load playlists from fs and store to DB
   toDB = async () => {
      const data = this.getLibrary();
      await data.forEach(item => {
         song.create(item);
      });

      const playlists = this.getPlaylists();
      playlists.forEach(item => {
         if (item !== undefined) {
            playlist.create(item);
         }
      });
   };

   _savePicturesInFolder = (url, pathname) => {
      const fullUrl = url;
      const file = fs.createWriteStream(pathname);
      const request = https.get(url, function(response) {
         response.pipe(file);
      });
   };

   loadPicturesForSong = () => {
      const data = this.getLibrary();
      const pathname = path.join(this._dataPath, "images");
      data.forEach(async song => {
         await fetch('http://ws.audioscrobbler.com/2.0/' +
             "?method=album.getinfo&api_key=b25b959554ed76058ac220b7b2e0a026" +
             "&artist=" + song.artist +
             "&album=" + song.album, {
         })
             .then(response => response.text())
             .then(response => {
               const dataAsJson = JSON.parse(convert.xml2json(response));
               try {
                  const urlImage = dataAsJson.elements[0].elements[0].elements[8].elements[0].text;
                  console.log(song.artist + " " + song.album + ": " + urlImage);
                  const nameImage = song.artist + "_" + song.album + ".jpg"
                  this._savePicturesInFolder(urlImage, path.join(pathname, nameImage));
               } catch (e) {
                  console.log("Not found album image");
               }
               return dataAsJson;
            });
      })
   };
}

exports.Import = new Import(path.join(__dirname, '..', '..', 'data'));
