import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div class="page-container">
        <NavBar />
      </div>
    );
  }
}

export default SearchArticle;
