import "./Playlists.css";
import React, { Component } from "react";
import { NoResults } from "../NoResults/NoResults";
import { TopBar } from "../TopBar/TopBar";
import { NewPlaylist } from "../NewPlaylist/NewPlaylist";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import { Playlist } from "../Playlist/Playlist";

const GET_PLAYLISTS = gql`
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
`

export class Playlists extends Component {
    constructor(props) {
        super(props);
        this.state = {
            trigger: false
        };
    }

    topBar = (refetch) => {
        return (
            <TopBar title="My Playlists">
                <NewPlaylist handlePlaylistsUpdating={() => {this.handlePlaylistsUpdating(refetch)}} />
            </TopBar>
        )
    }

    handlePlaylistsUpdating = async (refetch) => {
        const { trigger } = this.state;
        await refetch();
        this.setState({
            trigger: !trigger,
        });
        window.location.reload();
    }

    render() {
        const { newTrackInPlaylist } = this.props;

        return <Query query={GET_PLAYLISTS}>{({loading, error, data, refetch}) => {

            if (loading) return <NoResults message="Loading..."/>;
            if (error) return <p>Error :(</p>;
            if (data.playlists.count === 0) return <NoResults
                message="Fill free to create your personal playlists"/>;
            return <div className="playlistList">
                {!newTrackInPlaylist && this.topBar(refetch)}
                <div className="playlists">
                    {data.playlists.map((playlist, index) => (
                        <div key={index}>
                            <Playlist
                                handlePlaylistsUpdating={() => {this.handlePlaylistsUpdating(refetch)}}
                                newTrackInPlaylist={newTrackInPlaylist}
                                playlist={playlist} index={index}/>
                        </div>)
                    )}
                </div>
            </div>
        }}
        </Query>;
    }
}
