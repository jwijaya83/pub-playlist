import React from "react";
import "normalize.css/normalize.css";
import "./App.css";
import { AlbumList } from "../AlbumList/AlbumList";
import { Header } from "../Header/Header";

function App() {
  return (
    <>
      <Header />
      <AlbumList />
    </>
  );
}

export default App;
