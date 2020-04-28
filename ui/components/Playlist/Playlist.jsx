import React, {Component} from "react";
import "./Playlist.css";
import {Play} from "../Play/Play";
import {PlaylistTrack} from "../PlaylistTrack/PlaylistTrack";

export class Playlist extends Component {

    render() {
        const {playlist} = this.props

        return (
            <div className="Playlist" id={"playlist-" + playlist.id}>
                <div className="cover">
                    <div className="songs">
                        {playlist.songs.map((song, index) => (
                            <PlaylistTrack song={song} index={index} key={song.id}/>
                        ))}
                    </div>
                </div>
                <div className="name" title={playlist.name}>
                    {playlist.name}
                </div>
                <Play/>
            </div>
        );
    }
}