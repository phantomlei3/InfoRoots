import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";
import AuthorCard from "../AuthorCard/AuthorCard.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "Red Cross or BlackCross",
      author: "Dr.Marshall",
      publisher: "People's Publishing House",
      articleText:
        "Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.",
      authorCardToggled: false
    };
  }

  // Function to handle toggling the Author Card
  toggleAuthorCard = () => {
    if (this.state.authorCardToggled === false) {
      this.setState({ authorCardToggled: true });
    } else {
      this.setState({ authorCardToggled: false });
    }
  };

  render() {
    return (
      <div className="page-container">
        <NavBar />
        <div className="intro-container">
          <div id="text-container">
            <div id="title-container">{this.state.title}</div>
            <div id="author-container">
              Author:
              <div id="author-text" onClick={this.toggleAuthorCard}>
                {this.state.author}
              </div>
              {this.state.authorCardToggled && (
                <AuthorCard
                  author={this.state.author}
                  description="His interests are in decision making from data in complex systems, including machine learning, computational finance. He enjoys poker bridge squash..."
                  credibility={4.5}
                  authorLink="http://google.com"
                />
              )}
            </div>
            <div id="publisher-container">
              Publisher: <span>{this.state.publisher}</span>
            </div>
          </div>
        </div>
        <div className="bottom-container">
          <div id="article-container">
            <div id="article-text-container">"{this.state.articleText}</div>
          </div>
        </div>
      </div>
    );
  }
}

export default SearchArticle;
