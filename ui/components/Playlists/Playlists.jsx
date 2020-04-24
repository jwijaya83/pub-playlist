import "./Playlists.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";

export class Playlists extends Component {
  state = {
    playlists: [],
  };

  render() {
    const { playlists } = this.state

    return <div className="Playlists">
      {!playlists.length && <NoResults message="Fill free to create your personal playlists" />}
    </div>;
  }
}
