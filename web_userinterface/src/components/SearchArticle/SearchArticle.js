import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";
import AuthorCard from "../AuthorCard/AuthorCard.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: decodeURIComponent(this.props.match.params.articleUrl),
      title: this.props.location.state.title,
      author: this.props.location.state.author,
      publisher: this.props.location.state.publisher,
      articleText: this.props.location.state.articleText,
      authorCardToggled: this.props.location.state.authorCardToggled,
      author_name: this.props.location.state.author_name,
      author_introduction: this.props.location.state.author_introduction,
      author_reliability_score: this.props.location.state
        .author_reliability_score
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
                  author={this.state.author_name}
                  description={this.state.author_introduction}
                  credibility={this.state.author_reliability_score}
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
