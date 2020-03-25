import React from "react";
import "./Homepage.css";
import { Icon } from "@iconify/react";
import magnifyingGlass from "@iconify/icons-oi/magnifying-glass";
import InfoRootsLogo from "../../static/logo.png";

class Homepage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchQuery: ""
    };
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
      <div>
        <div id="top">
          <img src={InfoRootsLogo} id="logo" alt="InfoRoots Logo" />
        </div>
        <div id="bottom">
          <div id="homepage-search-bar">
            <input
              id="homepage-input"
              placeholder="Input the URL of the article you want to search..."
              value={this.state.searchQuery}
              type="text"
              onKeyPress={this.enterPressed}
              onChange={this.setSearchQuery}
            />
            <button id="homepage-button" onClick={this.handleSearch}>
              <Icon icon={magnifyingGlass} style={{ color: "white" }} />
            </button>
          </div>
          <div className="footer">
            <a
              href="https://github.com/phantomlei3/InfoRoots"
              id="about"
              target="_blank"
              rel="noopener noreferrer"
            >
              About
            </a>
            <div id="contact">Contact Us</div>
            <div id="developers">Developers</div>
          </div>
        </div>
      </div>
    );
  }
}

export default Homepage;
