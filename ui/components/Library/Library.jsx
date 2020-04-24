import "./Library.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";

export class Library extends Component {
  state = {
    tracks: [],
  };

  render() {
    const { tracks } = this.state

    return <div className="Library">
      {!tracks.length && <NoResults message="No tracks matched you search" />}
    </div>;
  }
}
