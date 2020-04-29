import React from 'react'
import './PlaylistTrack.css'

export const PlaylistTrack = ({song, index}) => (
    <div className="playlist-track">
        <div className="playlist-track-title" title={song.title}>
            <span className="number">{index + 1}</span>
            {song.title}
        </div>
        <button type="button" className="delete-from-playlist" title="Delete from Playlist">
            <span className="material-icons">delete</span>
        </button>
    </div>
)
