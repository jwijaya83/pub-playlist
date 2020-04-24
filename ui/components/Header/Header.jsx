import React from "react";
import "./Header.css";
import { Logo } from "../Logo/Logo";
import { Navigation } from "../Navigation/Navigation";

export const Header = () => (
  <header className="Header">
    <Logo />
    <Navigation />
  </header>
)

