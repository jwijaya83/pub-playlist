import React, { Component } from "react";
import "./Playlist.css";
import { Play } from "../Play/Play";
import { PlaylistTrack } from "../PlaylistTrack/PlaylistTrack";
import gql from "graphql-tag";
import { Mutation } from "react-apollo";

const ADD_SONG_TO_PLAYLIST = gql`
mutation EditPlaylist($id: Int!, $name: String, $songs: [Int]) {
    editPlaylist(id: $id, name: $name, songs: $songs) {
        id
    }
}
`;

const DELETE_PLAYLIST = gql`
mutation DeletePlaylist($id: Int!) {
    deletePlaylist(id: $id) {
        id
    }
}    
`;

export class Playlist extends Component {
    constructor(props) {
        super();
        this.state = {
            playlist: props.playlist,
            isEditName: false
        }
    }

    actionDeleteFromPlaylist = (songId) => {
        this.setState(prevState => ({
            playlist: {
                ...prevState.playlist,
                songs: this.state.playlist.songs.filter(song => song.id !== songId)
            }
        }));
        this.props.handlePlaylistsUpdating();
    };

    deletePlaylistButton = () => {
        return (
            <Mutation mutation={DELETE_PLAYLIST}>{(deletePlaylist, { _ }) => (
                <button type="button" className="delete-playlist"
                    onClick={e => {
                        e.preventDefault();
                        deletePlaylist({
                            variables: {
                                id: this.state.playlist.id
                            }
                        });
                    }} title="Delete playlist">
                    <span className="material-icons">delete</span>
                </button>
            )
            }</Mutation>
        )
    }

    createPlaylist = (playlist, editPlaylist) => {
        const { newTrackInPlaylist } = this.props;
        let prevSongs = playlist.songs.map(song => { return song.id });
        editPlaylist({
            variables: {
                id: playlist.id, name: playlist.name,
                songs: [...prevSongs, newTrackInPlaylist.track.id]
            }
        });
        playlist.songs.push(newTrackInPlaylist.track);
        newTrackInPlaylist.trackCallback();
    };

    editName = (e, playlist, editPlaylist) => {
        if (e.key === 'Enter') {
            editPlaylist({
                variables: {
                    id: playlist.id,
                    name: playlist.name
                }
            });
            this.props.handlePlaylistsUpdating();
            this.handleEditName(false);
        }
    };

    handleEditName = (status) => {
        this.setState({ isEditName: status });
    };

    changeName = (e) => {
        this.setState({ playlist: { ...this.state.playlist, name: e.target.value } });
    };

    render() {
        const { playlist, isEditName } = this.state;
        const { newTrackInPlaylist } = this.props;
        let play;
        let fromModal;
        if (!newTrackInPlaylist) {
            play = <Play />
        } else {
            fromModal = newTrackInPlaylist.fromModal
        }

        const addToPlaylistButton = () => {
            if (newTrackInPlaylist) {
                return (
                    <Mutation mutation={ADD_SONG_TO_PLAYLIST}>{(editPlaylist, { _ }) => (
                        <button type="button" className="btn-icon add add-button"
                            onClick={() => { this.createPlaylist(playlist, editPlaylist) }} title="Add">
                            <span className="material-icons add-button-icon">add</span>
                        </button>
                    )
                    }</Mutation>
                )
            }
        }

        const editNamePlaylist = () => {
            return <Mutation mutation={ADD_SONG_TO_PLAYLIST}>{(editPlaylist, { _ }) => (
                <div className="name" title={playlist.name} onClick={() => this.handleEditName(!newTrackInPlaylist && true)}>
                    {!isEditName && <div>{playlist.name}</div>}
                    {isEditName && !newTrackInPlaylist && <div className="edit-name">
                        <input value={playlist.name} autoFocus
                            onChange={this.changeName}
                            onKeyPress={(e) => this.editName(e, playlist, editPlaylist)}
                        />
                    </div>}
                    {!newTrackInPlaylist && <div className="edit"><span className="material-icons">edit</span></div>}
                </div>
            )}</Mutation>
        }

        return (
            <div className="Playlist" id={"playlist-" + playlist.id}>
                <div className="cover">
                    <div className="songs">
                        {addToPlaylistButton()}
                        {playlist.songs.map((song, index) => (
                            <PlaylistTrack playlist={playlist} playlistCallback={this.actionDeleteFromPlaylist}
                                fromModal={fromModal}
                                song={song} index={index} key={song.id} />
                        ))}
                    </div>
                </div>
                {editNamePlaylist()}
                {play}
                {this.deletePlaylistButton()}
            </div>
        );
    }
}
