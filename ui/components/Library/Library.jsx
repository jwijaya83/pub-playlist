import "./Library.css";
import React, {Component} from "react";
import { NoResults } from "../NoResults/NoResults";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import {Song} from "../Song/Song";
import {TopBar} from "../TopBar/TopBar";
import {Search} from "../Search/Search";

export class Library extends Component {

  constructor() {
    super();
    this.state = {
      title: ""
    }
  }

  _handleSearch = (value) => {
    this.setState({title: value});
  };

  render() {
    const {title} = this.state;

    return <div className="Library">
      <TopBar title="Search">
        <Search onChange={this._handleSearch} delay={500}/>
      </TopBar>
      <Query
          query={gql`
            query {
                libraries (search: "${title}") {
                    id,
                    title,
                    album,
                    artist,
                    duration
                }
            }
        `}
      >
        {({ loading, error, data }) => {
          if (loading) return <NoResults message="Loading..." />;
          if (error) return <p>Error :(</p>;

          return (
            <div className="libraries">
              {data.libraries.map((song, index) => (
                  <div key={song.id}><Song song={song} index={index} /></div>
              ))}
              {data.libraries.length === 0 && <NoResults message="Songs not found" />}
            </div>
          );
        }}
      </Query>
    </div>;
  }
}
