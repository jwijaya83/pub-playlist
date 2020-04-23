import React from 'react'
import './AlbumList.css'
import tracks from '../../assets/data/library.json'
import { shuffle } from '../../lib/shuffle'
import { Album } from '../Album/Album'

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
// shuffle(albums)

export const AlbumList = () => (
  <div className="album-list">
    {Object.keys(albums).map((albumName) => (
      <div key={albumName}><Album name={albumName} tracks={albums[albumName]} /></div>
    ))}
  </div>
)
