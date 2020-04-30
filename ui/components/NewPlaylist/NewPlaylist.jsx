import "./NewPlaylist.css";
import React, {Component} from "react";
import gql from "graphql-tag";
import {Mutation} from "react-apollo";

const CREATE_PLAYLIST = gql`
    mutation CreatePlaylist($name: String!) {
        createPlaylist(name: $name) {
            id
        }
    }
`;

export class NewPlaylist extends Component {
    constructor(props) {
        super(props);
        this.handlePlaylistsUpdating = props.handlePlaylistsUpdating
    }

    state = {
        isAdding: false,
        newPlaylistName: ''
    };

    handleAddClick() {
        this.setState({
            isAdding: true,
        })
    }

    handleCancelClick() {
        this.setState({
            isAdding: false,
            newPlaylistName: ''
        })
    }

    render() {
        const {isAdding} = this.state;

        if (isAdding) {
            return (
                <div className="NewPlaylist">
                    <input type="text" value={this.state.newPlaylistName}
                           onChange={(e) => this.setState({newPlaylistName: e.target.value})}
                           placeholder="Playlist Name" className="playlist-name" autoFocus/>
                    <Mutation mutation={CREATE_PLAYLIST} ignoreResults={false}>{(createPlaylist) => (
                        <button type="button" className="btn-icon create" title="Create Playlist" onClick={e => {
                            e.preventDefault();
                            createPlaylist({variables: {name: this.state.newPlaylistName}}).then(({data}) => {
                                console.log("create playlist");
                                this.handlePlaylistsUpdating()
                                this.handleCancelClick()
                            });
                        }}>
                            <span className="material-icons">done</span>
                        </button>)
                    }</Mutation>
                    <button type="button" className="btn-icon cancel" onClick={() => this.handleCancelClick()}
                            title="Cancel">
                        <span className="material-icons">clear</span>
                    </button>
                </div>
            )
        } else {
            return (
                <div className="NewPlaylist">
                    <button type="button" className="btn-icon start" title="Create New Playlist"
                            onClick={() => this.handleAddClick()}>
                        <span className="material-icons">add</span>
                    </button>
                </div>
            );
        }
    }
}
