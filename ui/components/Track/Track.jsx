import React, { Component } from "react";
import './Track.css';
import {AddSongModal} from "../AddSongModal/AddSongModal";

export class Track extends Component {

  constructor() {
    super();
    this.state = {
      isModalShown: false
    };
  }

  actionModalPlaylists = () => {
    this.setState({ isModalShown: !this.state.isModalShown });
  }

  render() {
    const { track } = this.props;
    let newTrackInPlaylist = {
      track: track,
      trackCallback: this.actionModalPlaylists,
      fromModal: true
    }
    return (
      <div className="track">
        <div className="track-title" title={track.title}>
          <span className="number">{this.props.index + 1}</span>
          {track.title}
        </div>
        <button type="button" className="add-to-playlist" title="Add to Playlist">
          <span className="material-icons" onClick={this.actionModalPlaylists}>add</span>
        </button>
        <AddSongModal isShow={this.state.isModalShown}
                      newTrackInPlaylist={newTrackInPlaylist}
                      closePlaylist={this.actionModalPlaylists}
        />
      </div>
    )
  }

}
