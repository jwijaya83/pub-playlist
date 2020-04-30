import React, {useState} from "react";
import "./Song.css";
import { Play } from "../Play/Play";
import {AddSongModal} from "../AddSongModal/AddSongModal";

export const Song = ({ song, index }) => {
    let [isShowModal, setShowModal] = useState(false);
    const songStyle = {
        backgroundImage: `url('/images/${song.artist}_${song.album}.jpg')`,
    };
    const actionModalPlaylists = () => {
        setShowModal(!isShowModal);
    };
    let newTrackInPlaylist = {
        track: song,
        trackCallback: actionModalPlaylists,
        fromModal: true
    }

    return (
        <div className="Song" id={"Song-" + song.id} >
            <div className="song songs" style={songStyle}>
                <button type="button" className="btn-icon add add-button" title="Add"
                    onClick={actionModalPlaylists}>
                    <span className="material-icons add-button-icon">add</span>
                </button>
            </div>
            <div className="name" title={song.title}>
                {song.title}
            </div>
            <div className="artist" title={song.artist}>
                {song.artist}
            </div>
            <div className="album" title={song.album}>
                {song.album}
            </div>
            <div className="duration" title={song.duration}>
                Duration: {song.duration}
            </div>
            <Play />
            {isShowModal && <AddSongModal isShow={isShowModal}
                          newTrackInPlaylist={newTrackInPlaylist}
                          closePlaylist={actionModalPlaylists}
            />}
        </div>
    );
};
