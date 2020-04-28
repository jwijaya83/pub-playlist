import React from "react";
import "./Song.css";
import { Play } from "../Play/Play";

export const Song = ({ song, index }) => {
    const coverStyle = {
        backgroundImage: `url(/images/cover-${(index % 4) + 1}.jpg)`,
    };

    return (
        <div className="Song" id={"Song-" + song.id}>
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
        </div>
    );
};
