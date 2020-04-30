import React from 'react';
import './AddSongModal.css';
import {Playlists} from "../Playlists/Playlists";
import Modal from "react-modal";

export const AddSongModal = ({newTrackInPlaylist, isShow, closePlaylist}) => {
    Modal.setAppElement('body');
    return <Modal
        isOpen={isShow}>
        <button type="button" className="btn-icon close close-button" onClick={closePlaylist} title="Close">
            <span className="material-icons">close</span>
        </button>
        <div className="gap"/>
        <Playlists newTrackInPlaylist={newTrackInPlaylist} />
    </Modal>
};
