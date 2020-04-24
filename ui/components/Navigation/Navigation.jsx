import React from "react";
import "./Navigation.css";
import { NavLink } from "react-router-dom";

export const Navigation = () => (
  <nav className="Navigation">
    <NavLink className="link" to="/" activeClassName="active" exact>Albums</NavLink>
    <NavLink className="link" to="/playlists" activeClassName="active">Playlists</NavLink>
    <NavLink className="link" to="/library" activeClassName="active">Library</NavLink>
  </nav>
);
