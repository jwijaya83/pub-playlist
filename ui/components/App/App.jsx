import React from "react";
import "normalize.css/normalize.css";
import "./App.css";
import { AlbumList } from "../AlbumList/AlbumList";
import { Logo } from "../Logo/Logo";

function App() {
  return (
    <>
      <Logo />
      <AlbumList />
    </>
  );
}

export default App;
