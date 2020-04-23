import React from 'react'
import './Track.css'

export const Track = ({ track }) => (
  <div className="track">
    <div className="track-title" title={track.title}>{track.title}</div>
    <button type="button" className="add-to-playlist" title="Add to Playlist">
      <span class="material-icons">add</span>
    </button>
  </div>
)
