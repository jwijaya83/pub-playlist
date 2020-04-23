import React from "react";
import "./Album.css";
import { Track } from "../Track/Track";
import { Play } from "../Play/Play";

export const Album = ({ name, tracks, index }) => {
  const coverStyle = {
    backgroundImage: `url(/images/cover-${(index % 4) + 1}.jpg)`,
  };

  return (
    <div className="Album" id={"album-" + tracks[0].id}>
      <div className="cover" style={coverStyle}>
        <div className="tracks">
          {tracks.map((track) => (
            <Track track={track} />
          ))}
        </div>
      </div>
      <div className="name" title={name}>
        {name}
      </div>
      <div className="artist" title={tracks[0].artist}>
        {tracks[0].artist}
      </div>
      <Play />
    </div>
  );
};
