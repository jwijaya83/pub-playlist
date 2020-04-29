import "./Library.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import {Song} from "../Song/Song";

export class Library extends Component {

  render() {
    return <Query
          query={gql`
            query {
                libraries {
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
              <div className="Library">
                <div className="libraries">
                  {data.libraries.map((song, index) => (
                      <div key={song.id}><Song song={song} index={index} /></div>
                  ))}
                </div>
              </div>
          );
        }}
      </Query>;
  }
}
