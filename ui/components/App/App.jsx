import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import "normalize.css/normalize.css";
import "./App.css";
import { Header } from "../Header/Header";
import { Routes } from "../Routes/Routes";
import { ApolloProvider } from 'react-apollo';
import ApolloClient from 'apollo-boost';

const client = new ApolloClient({
    uri: 'http://127.0.0.1:3000',
});

function App() {
  return (
      <ApolloProvider client={client}>
        <Router>
          <Header />
          <Routes />
        </Router>
      </ApolloProvider>
  );
}

export default App;
