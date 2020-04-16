import React from "react";
import "./SearchArticle.css";
import Rater from "react-rater";
import "react-rater/lib/react-rater.css";
import NavBar from "../NavBar/NavBar.js";
import AuthorCard from "../AuthorCard/AuthorCard.js";
import PublisherCard from "../PublisherCard/PublisherCard.js";
import Citation from "../Citation/Citation.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: decodeURIComponent(this.props.match.params.articleUrl),
      title: this.props.location.state.title,
      article_text: this.props.location.state.article_text,
      article_reliability_score: this.props.location.state
        .article_reliability_score,
      article_paragraphs: this.props.location.state.article_paragraphs,
      citation_links: this.props.location.state.citation_links,
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

  // Function to handle citations in the article text
  renderArticleText = () => {
    var elements = [];
    for (let i = 0; i < this.state.article_paragraphs.length; i++) {
      console.log(this.state.article_paragraphs[i]);
      elements.push(
        <Citation
          key={i}
          link={this.state.citation_links[i]}
          paragraph={this.state.article_paragraphs[i].substr(
            0,
            this.state.article_paragraphs[i].length
          )}
        />
      );
    }
    return elements;
  };

  render() {
    var articleText = this.renderArticleText();
    return (
      <div className="page-container">
        <NavBar />
        <div className="intro-container">
          <div id="text-container">
            <div id="title-container">
              {this.state.title}
              <div id="stars">
                <Rater
                  total={5}
                  interactive={false}
                  rating={this.state.article_reliability_score * 5}
                />
              </div>
            </div>
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
            <div id="article-text-container">{articleText}</div>
          </div>
        </div>
      </div>
    );
  }
}

export default SearchArticle;
