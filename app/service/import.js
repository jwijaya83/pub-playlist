const path = require('path');
const Songs = require('../../lib/songs');
const library = new Songs(path.join(__dirname, '..', '..', 'data'));
const song = require('../repository/song');


var data = library.getLibrary();
data.forEach(item => {
   song.create(item)
});
