import React from "react";
import "./NavBar.css";
import { Icon } from "@iconify/react";
import magnifyingGlass from "@iconify/icons-oi/magnifying-glass";
import InfoRootsLogo from "../../static/logo.png";
import MenuImage from "../../static/menu.svg";

class NavBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { searchQuery: "" };
  }

  // Function to handle searching of a URL on the homepage
  handleSearch = () => {
    if (this.state.searchQuery.length === 0) {
      return;
    }

    console.log("Searched: '" + this.state.searchQuery + "'");
  };

  setSearchQuery = event => {
    this.setState({
      searchQuery: event.target.value
    });
  };

  // Handle when the user presses enter to search
  enterPressed = event => {
    var code = event.which;
    if (code === 13) {
      this.handleSearch();
    }
  };

  render() {
    return (
      <div class="navbar">
        <div id="searchbar-container">
          <input
            placeholder="Search an article..."
            id="searcharticle-input-bar"
            value={this.state.searchQuery}
            type="text"
            onKeyPress={this.enterPressed}
            onChange={this.setSearchQuery}
          />
          <button id="searcharticle-button" onClick={this.handleSearch}>
            <Icon icon={magnifyingGlass} style={{ color: "white" }} />
          </button>
        </div>
        <div id="logo-container">
          <img id="navbar-logo" src={InfoRootsLogo} alt="InfoRoots Logo" />
        </div>
        <div id="menuimage-container">
          <img id="menuimage" src={MenuImage} />
        </div>
      </div>
    );
  }
}

export default NavBar;
