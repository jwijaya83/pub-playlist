import React from 'react'
import './AlbumList.css'
import { Album } from '../Album/Album'
import { TopBar } from '../TopBar/TopBar'
import gql from "graphql-tag";
import {NoResults} from "../NoResults/NoResults";
import {Query} from "react-apollo";
import _ from "lodash";

const GET_SONGS = gql`
            query {
                libraries {
                    id,
                    title,
                    album,
                    artist
                }
            }
        `

export const AlbumList = () => (
  <div className="AlbumList">
    <TopBar title="Top Albums" />
      <Query query={GET_SONGS}>
          {({ loading, error, data }) => {
              if (loading) return <NoResults message="Loading..."/>;
              if (error) return <p>Error :(</p>;
              data = _.groupBy(data.libraries, item => item.album);

              return <div className="albums">
                  {_.map(data, (songs, album) => {
                      return <div key={album}><Album name={album} tracks={songs} index={album} /></div>;
                  })}
              </div>;
          }}
      </Query>
  </div>
);
