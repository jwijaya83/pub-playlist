import "./NewPlaylist.css";
import React, { Component } from "react";

export class NewPlaylist extends Component {
  state = {
    isAdding: false,
  };

  handleAddClick() {
    this.setState({
      isAdding: true,
    })
  }

  handleCancelClick() {
    this.setState({
      isAdding: false,
    })
  }

  render() {
    const { isAdding } = this.state;

    if (isAdding) {
      return (
        <div className="NewPlaylist">
          <input type="text" placeholder="Playlist Name" className="playlist-name" autoFocus />
          <button type="button" className="btn-icon create" title="Create Playlist">
            <span className="material-icons">done</span>
          </button>
          <button type="button" className="btn-icon cancel" onClick={() => this.handleCancelClick()} title="Cancel">
            <span className="material-icons">clear</span>
          </button>
        </div>
      )
    } else {
      return (
        <div className="NewPlaylist">
          <button type="button" className="btn-icon start" title="Create New Playlist" onClick={() => this.handleAddClick()}>
            <span className="material-icons">add</span>
          </button>
        </div>
      );
    }
  }
}
