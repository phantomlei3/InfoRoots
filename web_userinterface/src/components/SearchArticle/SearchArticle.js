import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "Red Cross or BlackCross",
      author: "Dr.Marshall",
      publisher: "People's Publishing House",
      articleText:
        "Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people.Chongqing, China The Wuhan Red Cross and Hubei provincial Red Cross have come under fire after donations of crucial medical supplies from across China failed to arrive at the hospitals on the front lines of a coronavirus outbreak that has killed more than 300 people."
    };
  }

  render() {
    return (
      <div className="page-container">
        <NavBar />
        <div className="intro-container">
          <div id="text-container">
            <div id="title-container">{this.state.title}</div>
            <div id="author-container">
              Author: <span>{this.state.author}</span>
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
