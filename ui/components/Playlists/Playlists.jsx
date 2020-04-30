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
        this.handlePlaylistsUpdating = this.handlePlaylistsUpdating.bind(this);
        this.isNewPlaylistCreated = false
        this.playlists = Array(0)
        this.state = {
            trigger: false
        };
    }

    topBar() {
        return (
            <TopBar title="My Playlists">
                <NewPlaylist handlePlaylistsUpdating={this.handlePlaylistsUpdating}/>
            </TopBar>
        )
    }

    handlePlaylistsUpdating(playlist) {
        this.isNewPlaylistCreated = true
        this.playlists.push(playlist);
        this.forceUpdate()
    }

    componentDidMount() {
        if (this.isNewPlaylistCreated) {
            this.isNewPlaylistCreated = false
        }
    }

    createPlaylists(playlists) {
        let topBar;
        if (!this.props.newTrackInPlaylist) {
            topBar = this.topBar()
        }
        return (<div className="playlistList">
            {topBar}
            <div className="playlists">
                {playlists.map((playlist, index) => (
                    <div key={index}><Playlist newTrackInPlaylist={this.props.newTrackInPlaylist}
                                               playlist={playlist} index={index}/></div>
                ))}
            </div>
        </div>);
    }

    render() {
        return <Query query={GET_PLAYLISTS}>{({loading, error, data}) => {
            if (loading) return <NoResults message="Loading..."/>;
            if (error) return <p>Error :(</p>;
            if (data.playlists.count === 0) return <NoResults
                message="Fill free to create your personal playlists"/>;

            if (!this.isNewPlaylistCreated) {
                this.playlists = Array(0).concat(data.playlists)
            }

            return this.createPlaylists(this.playlists);
        }}
        </Query>;
    }
}
