import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import "normalize.css/normalize.css";
import "./App.css";
import { Header } from "../Header/Header";
import { Routes } from "../Routes/Routes";

function App() {
  return (
    <Router>
      <Header />
      <Routes />
    </Router>
  );
}

export default App;
