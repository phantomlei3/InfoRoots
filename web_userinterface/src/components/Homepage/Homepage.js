import React from "react";
import { Redirect } from "react-router-dom";
import "./Homepage.css";
import { Icon } from "@iconify/react";
import magnifyingGlass from "@iconify/icons-oi/magnifying-glass";
import InfoRootsLogo from "../../static/logo.png";
import {
  processUserSearch,
  handleSearch,
  renderArticlePage,
  setSearchQuery,
  enterPressed
} from "../../api.js";

class Homepage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchQuery: "",
      articleSearched: false
    };
  }

  processUserSearch = processUserSearch.bind(this);
  handleSearch = handleSearch.bind(this);
  renderArticlePage = renderArticlePage.bind(this);
  setSearchQuery = setSearchQuery.bind(this);
  enterPressed = enterPressed.bind(this);

  render() {
    return (
      <div>
        {this.renderArticlePage()}
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
