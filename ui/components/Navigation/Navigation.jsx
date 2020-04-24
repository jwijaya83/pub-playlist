import React from "react";
import "./Navigation.css";

export const Navigation = () => (
  <nav className="Navigation">
    <a className="link active" href="/">Albums</a>
    <a className="link" href="/playlists">Playlists</a>
    <a className="link" href="/playlists">Library</a>
  </nav>
);
