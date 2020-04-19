import React from "react";
import "./AuthorCard.css";
import Rater from "react-rater";
import "react-rater/lib/react-rater.css";

class AuthorCard extends React.Component {
  render() {
    return (
      <div className="author_card">
        <div id="author">
          <div id="author-name">{this.props.author}</div>
          <div id="author-profile-link">
            <a
              id="author-link-a"
              href="https://github.com/phantomlei3/InfoRoots"
              target="_blank"
              rel="noopener noreferrer"
            >
              See verified profile
            </a>
          </div>
        </div>
        <div id="description">{this.props.description}</div>
        <div id="credibility">
          <span id="credibility-text">credibility</span>
          <Rater
            total={5}
            interactive={false}
            rating={this.props.credibility * 5}
          />
        </div>
      </div>
    );
  }
}

export default AuthorCard;
