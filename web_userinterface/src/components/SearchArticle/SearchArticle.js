import React from "react";
import "./SearchArticle.css";
import NavBar from "../NavBar/NavBar.js";
import AuthorCard from "../AuthorCard/AuthorCard.js";
import { getArticle, getAuthor } from "../../api.js";

class SearchArticle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: decodeURIComponent(this.props.match.params.articleUrl),
      title: "",
      author: "",
      publisher: "",
      articleText: "",
      authorCardToggled: false,
      author_name: "",
      author_introduction: "",
      author_reliability_score: 0
    };

    // Obtain article information
    getArticle(this.state.url).then(res => {
      this.setState({
        title: res.data.article_title,
        articleText: res.data.article_content,
        author: res.data.author_name,
        publisher: res.data.publisher_name
      });
    });

    // Obtain author information
    getAuthor(this.state.url).then(res => {
      this.setState({
        author_name: res.data.author_name,
        author_introduction: res.data.author_introduction,
        author_reliability_score: res.data.author_reliability_score
      });
    });

    console.log(this.state.author);
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
