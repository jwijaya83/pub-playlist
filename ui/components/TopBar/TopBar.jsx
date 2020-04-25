import "./TopBar.css";
import React, { Component } from "react";

export class TopBar extends Component {
  render() {
    const { title, children } = this.props
    return (
      <div className="TopBar">
        <h1 className="page-title">{title}</h1>
        { children }
      </div>
    );
  }
}
