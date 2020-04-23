import React from 'react'
import './Album.css'

export const Album = ({ name, tracks }) => (
  <div className="Album" id={'album-' + tracks[0].id}>
    <div className="cover"></div>
    <div className="name">{name}</div>
    <div className="artist">{tracks[0].artist}</div>
    <button type="button" className="play"></button>
  </div>
)
