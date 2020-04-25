import "./Playlists.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";
import { TopBar } from "../TopBar/TopBar";
import { NewPlaylist } from "../NewPlaylist/NewPlaylist";

export class Playlists extends Component {
  state = {
    playlists: [],
  };

  render() {
    const { playlists } = this.state

    return <div className="Playlists">
      <TopBar title="My Playlists">
        <NewPlaylist />
      </TopBar>
      {!playlists.length && <NoResults message="Fill free to create your personal playlists" />}
    </div>;
  }
}
