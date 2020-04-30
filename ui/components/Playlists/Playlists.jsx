import "./Playlists.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";
import { TopBar } from "../TopBar/TopBar";
import { NewPlaylist } from "../NewPlaylist/NewPlaylist";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import { Playlist } from "../Playlist/Playlist";

export class Playlists extends Component {

    topBar() {
        return (
            <TopBar title="My Playlists">
                <NewPlaylist />
            </TopBar>
        )
    }

    render() {
        let topBar;
        if (!this.props.newTrackInPlaylist) {
            topBar = this.topBar()
        }
        return <Query query={gql`
            query {
                playlists {
                    id,
                    name,
                    songs {
                        id,
                        album,
                        duration,
                        title,
                        artist
                    }
                }
            }
        `}
        >
            {({ loading, error, data }) => {
                if (loading) return <NoResults message="Loading..." />;
                if (error) return <p>Error :(</p>;
                if (data.playlists.count === 0) return <NoResults
                    message="Fill free to create your personal playlists" />

                return (
                    <div className="playlistList">
                        {topBar}
                        <div className="playlists">
                            {data.playlists.map((playlist, index) => (
                                <div key={index}><Playlist newTrackInPlaylist={this.props.newTrackInPlaylist}
                                    playlist={playlist} index={index} /></div>
                            ))}
                        </div>
                    </div>
                );
            }}
        </Query>;
    }
}
