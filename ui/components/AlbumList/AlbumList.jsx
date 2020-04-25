import React from 'react'
import './AlbumList.css'
import tracks from '../../assets/data/library.json'
import { shuffle } from '../../lib/shuffle'
import { Album } from '../Album/Album'
import { TopBar } from '../TopBar/TopBar'

const albums = tracks.reduce((acc, track) => {
  if (acc[track.album]) {
    acc[track.album] = [
      ...acc[track.album],
      track,
    ]
  } else {
    acc[track.album] = [track]
  }
  return acc
}, {})
const shuffledAlbums = shuffle(Object.keys(albums)).reduce((acc, albumName) => {
  acc[albumName] = albums[albumName]
  return acc
}, {})
shuffle(albums)

export const AlbumList = () => (
  <div className="AlbumList">
    <TopBar title="Top Albums" />
    <div className="albums">
      {Object.keys(shuffledAlbums).map((albumName, index) => (
        <div key={albumName}><Album name={albumName} tracks={albums[albumName]} index={index} /></div>
      ))}
    </div>
  </div>
)
