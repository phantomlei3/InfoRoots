import React from "react";
import "./Menu.css";

class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div id="menu">
        <div id="arrow-up"></div>
        <div id="drop-down">
          <div id="option">
            <a
              href="https://github.com/phantomlei3/InfoRoots"
              target="_blank"
              rel="noopener noreferrer"
            >
              settings
            </a>
          </div>
          <div id="option">
            <a
              href="https://github.com/phantomlei3/InfoRoots"
              id="option"
              target="_blank"
              rel="noopener noreferrer"
            >
              login
            </a>
          </div>
          <div id="option">
            <a
              href="https://github.com/phantomlei3/InfoRoots"
              id="option"
              target="_blank"
              rel="noopener noreferrer"
            >
              report
            </a>
          </div>
          <div id="option">
            <a
              href="https://github.com/phantomlei3/InfoRoots"
              id="option"
              target="_blank"
              rel="noopener noreferrer"
            >
              dataset
            </a>
          </div>
        </div>
      </div>
    );
  }
}

export default Menu;
