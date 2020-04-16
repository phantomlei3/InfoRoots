import React from "react";
import "./PublisherCard.css";
import Rater from "react-rater";
import "react-rater/lib/react-rater.css";

class PublisherCard extends React.Component {
  render() {
    return (
      <div className="publisher-card">
        <div id="publisher">
          <div id="publisher-name">{this.props.publisher_name}</div>
          <div id="publisher-profile-link">
            <a
              id="publisher-link-a"
              href="https://github.com/phantomlei3/InfoRoots"
              target="_blank"
              rel="noopener noreferrer"
            >
              View publisher site
            </a>
          </div>
        </div>
        <div id="description">{this.props.publisher_introduction}</div>
        <div id="credibility">
          credibility
          <Rater total={5} interactive={false} rating={0.8 * 5} />
        </div>
      </div>
    );
  }
}

export default PublisherCard;
