import React from 'react'
import './Track.css'

export const Track = ({ track, index }) => (
  <div className="track">
    <div className="track-title" title={track.title}>
      <span className="number">{index + 1}</span>
      {track.title}
    </div>
    <button type="button" className="add-to-playlist" title="Add to Playlist">
      <span className="material-icons">add</span>
    </button>
  </div>
)
