import React from "react";
import { Redirect } from "react-router-dom";
import "./NavBar.css";
import { Icon } from "@iconify/react";
import magnifyingGlass from "@iconify/icons-oi/magnifying-glass";
import InfoRootsLogo from "../../static/logo.png";
import MenuImage from "../../static/menu.svg";
import Menu from "../Menu/Menu.js";
import {
  processUserSearch,
  handleSearch,
  renderArticlePage,
  setSearchQuery,
  enterPressed
} from "../../api.js";

class NavBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchQuery: "",
      menuToggled: false,
      redirectToHome: false,
      articleSearched: false
    };
  }

  processUserSearch = processUserSearch.bind(this);
  handleSearch = handleSearch.bind(this);
  renderArticlePage = renderArticlePage.bind(this);
  setSearchQuery = setSearchQuery.bind(this);
  enterPressed = enterPressed.bind(this);

  // Function to handle toggling the menu
  toggleMenu = () => {
    if (this.state.menuToggled === false) {
      this.setState({ menuToggled: true });
    } else {
      this.setState({ menuToggled: false });
    }
  };

  // Clicked on homebutton
  handleHomeButton = () => {
    if (this.state.redirectToHome === false) {
      this.setState({ redirectToHome: true });
    }
  };

  // Function to handle routing back to the Homepage
  returnToHome = () => {
    if (this.state.redirectToHome === true) return <Redirect to={"/"} />;
  };

  render() {
    return (
      <div id="container">
        {this.returnToHome()}
        {this.renderArticlePage()}
        <div className="navbar">
          <div id="searchbar-container">
            <input
              placeholder="https://yourarticle..."
              id="searchbar-input"
              value={this.state.searchQuery}
              type="text"
              onKeyPress={this.enterPressed}
              onChange={this.setSearchQuery}
            />
            <button id="searchbar-button" onClick={this.handleSearch}>
              <Icon
                icon={magnifyingGlass}
                style={{ color: "white" }}
                alt="Search logo"
              />
            </button>
          </div>
          <div id="logo-container">
            <img
              id="navbar-logo"
              src={InfoRootsLogo}
              alt="InfoRoots Logo"
              onClick={this.handleHomeButton}
            />
          </div>
          <div id="menuimage-container">
            <img
              id="menuimage"
              src={MenuImage}
              alt="Menu"
              onClick={this.toggleMenu}
            />
          </div>
          {this.state.menuToggled && <Menu />}
        </div>
      </div>
    );
  }
}

export default NavBar;
