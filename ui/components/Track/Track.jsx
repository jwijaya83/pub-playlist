import React from 'react'
import './Track.css'

export const Track = ({ track }) => (
  <div className="track">
    <div className="name">{track.title}</div>
    <div className="artist">{track.artist}</div>
    <div className="album">{track.album}</div>
  </div>
)
