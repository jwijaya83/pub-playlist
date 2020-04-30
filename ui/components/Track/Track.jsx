import React, { Component } from "react";
import './Track.css';
import Modal from 'react-modal';
import { Playlists } from "../Playlists/Playlists";

export class Track extends Component {

  constructor() {
    super();
    this.state = {
      isModalShown: false
    };
    this.trackCallback = this.hidePlaylists.bind(this);
  }

  showPlaylists() {
    this.setState({ isModalShown: true });
  }

  hidePlaylists() {
    this.setState({ isModalShown: false });
  }

  render() {
    const { track } = this.props;
    let newTrackInPlaylist = {
      track: track,
      trackCallback: this.trackCallback,
      fromModal: true
    }
    return (
      <div className="track">
        <div className="track-title" title={track.title}>
          <span className="number">{this.props.index + 1}</span>
          {track.title}
        </div>
        <button type="button" className="add-to-playlist" title="Add to Playlist">
          <span className="material-icons" onClick={() => this.showPlaylists()}>add</span>
        </button>
        <Modal
          isOpen={this.state.isModalShown}>
          <button type="button" className="btn-icon close close-button" onClick={() => this.hidePlaylists()} title="Close">
            <span className="material-icons">close</span>
          </button>
          <div className="gap"></div>
          <Playlists newTrackInPlaylist={newTrackInPlaylist} />
        </Modal>
      </div>
    )
  }

}
