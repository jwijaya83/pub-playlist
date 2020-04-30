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

export class Playlist extends Component {

    addToPlaylistButton(playlist) {
        if (this.props.newTrackInPlaylist) {
            return (
                <Mutation mutation={ADD_SONG_TO_PLAYLIST}>{(editPlaylist, { _ }) => (
                    <button type="button" className="btn-icon add add-button"
                        onClick={e => {
                            e.preventDefault();
                            let prevSongs = playlist.songs.map(song => { return song.id });
                            editPlaylist({
                                variables: {
                                    id: playlist.id, name: playlist.name,
                                    songs: [...prevSongs, this.props.newTrackInPlaylist.track.id]
                                }
                            });
                            playlist.songs.push(this.props.newTrackInPlaylist.track);
                            this.props.newTrackInPlaylist.trackCallback();
                        }} title="Add">
                        <span className="material-icons add-button-icon">add</span>
                    </button>
                )
                }</Mutation>
            )
        }
    }

    render() {
        const { playlist } = this.props
        let play;
        let fromModal;
        if (!this.props.newTrackInPlaylist) {
            play = <Play />
        } else {
            fromModal = this.props.newTrackInPlaylist.fromModal
        }

        return (
            <div className="Playlist" id={"playlist-" + playlist.id}>
                <div className="cover">
                    <div className="songs">
                        {this.addToPlaylistButton(playlist)}
                        {playlist.songs.map((song, index) => (
                            <PlaylistTrack
                                fromModal={fromModal}
                                song={song} index={index} key={song.id} />
                        ))}
                    </div>
                </div>
                <div className="name" title={playlist.name}>
                    {playlist.name}
                </div>
                {play}
            </div>
        );
    }
}