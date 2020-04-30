import React, { Component } from "react";
import './PlaylistTrack.css';
import gql from "graphql-tag";
import { Mutation } from "react-apollo";

const DELETE_SONG_FROM_PLAYLIST = gql`
mutation EditPlaylist($id: Int!, $name: String, $songs: [Int]) {
    editPlaylist(id: $id, name: $name, songs: $songs) {
        id
    }
}
`;

export class PlaylistTrack extends Component {

    deleteFromPlaylistButton(playlist, songId) {
        return (
            <Mutation mutation={DELETE_SONG_FROM_PLAYLIST}>{(editPlaylist, { _ }) => (
                <button type="button" className="delete-from-playlist"
                    onClick={e => {
                        e.preventDefault();
                        let songIds = playlist.songs.map(song => { return song.id });
                        var index = songIds.indexOf(songId);
                        if (index > -1)
                            songIds.splice(index, 1);
                        editPlaylist({
                            variables: {
                                id: playlist.id, name: playlist.name,
                                songs: songIds
                            }
                        });
                        this.props.playlistCallback(songId);
                    }} title="Delete from Playlist">
                    <span className="material-icons">delete</span>
                </button>
            )
            }</Mutation>
        )
    }

    render() {
        let deleteButton;
        if (!this.props.fromModal) {
            deleteButton = this.deleteFromPlaylistButton(this.props.playlist, this.props.song.id);
        }
        return (
            <div className="playlist-track">
                <div className="playlist-track-title" title={this.props.song.title}>
                    <span className="number">{this.props.index + 1}</span>
                    {this.props.song.title}
                </div>
                {deleteButton}
            </div>
        );
    }
}
