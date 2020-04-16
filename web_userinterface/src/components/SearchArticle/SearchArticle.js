import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";
import AuthorCard from "../AuthorCard/AuthorCard.js";
import PublisherCard from "../PublisherCard/PublisherCard.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: decodeURIComponent(this.props.match.params.articleUrl),
      title: this.props.location.state.title,
      articleText: this.props.location.state.articleText,
      author_name: this.props.location.state.author_name,
      author_introduction: this.props.location.state.author_introduction,
      author_reliability_score: this.props.location.state
        .author_reliability_score,
      publisher_name: this.props.location.state.publisher_name,
      publisher_introduction: this.props.location.state.publisher_introduction,
      authorCardToggled: false,
      publisherCardToggled: false
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

  // Function to handle toggling the Publisher Card
  togglePublisherCard = () => {
    if (this.state.publisherCardToggled === false) {
      this.setState({ publisherCardToggled: true });
    } else {
      this.setState({ publisherCardToggled: false });
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
                {this.state.author_name}
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
              Publisher:
              <div id="publisher-text" onClick={this.togglePublisherCard}>
                {this.state.publisher_name}
              </div>
              {this.state.publisherCardToggled && (
                <PublisherCard
                  publisher_name={this.state.publisher_name}
                  publisher_introduction={this.state.publisher_introduction}
                  credibility={0.7}
                  publisherLink="http://google.com"
                />
              )}
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
