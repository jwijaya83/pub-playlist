import React from "react";
import { Switch, Route } from "react-router-dom";
import { Playlists } from "../Playlists/Playlists";
import { Library } from "../Library/Library";
import { AlbumList } from "../AlbumList/AlbumList"

export const Routes = () => (
  <Switch>
    <Route exact path="/">
      <AlbumList />
    </Route>
    <Route path="/playlists">
      <Playlists />
    </Route>
    <Route path="/library">
      <Library />
    </Route>
  </Switch>
);
