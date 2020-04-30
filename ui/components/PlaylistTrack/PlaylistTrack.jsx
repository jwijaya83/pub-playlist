import React, { Component } from "react";
import './PlaylistTrack.css'

export class PlaylistTrack extends Component {

    render() {
        let deleteButton;
        if (!this.props.fromModal) {
            deleteButton = (
                <button type="button" className="delete-from-playlist" title="Delete from Playlist">
                    <span className="material-icons">delete</span>
                </button>
            )
        }
        return (
            <div className="playlist-track">
                <div className="playlist-track-title" title={this.props.song.title}>
                    <span className="number">{this.props.index + 1}</span>
                    {this.props.song.title}
                </div>
                {deleteButton}
            </div>
        );
    }
}
