import React from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Redirect } from "react-router-dom";
import {
  getArticle,
  getAuthor,
  getPublisher,
  getCitationInformation
} from "../../api.js";
import "./LoadingPage.css";
import InfoRootsLogo from "../../static/logo.png";

class LoadingPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: props.location.state.url,
      title: "",
      article_text: "",
      article_reliability_score: "",
      author_name: "",
      author_introduction: "",
      author_reliability_score: 0,
      publisher_name: "",
      publisher_introduction: "",
      article_paragraphs: [],
      citation_links: [],
      citation_information: [],
      recievedResponse: false
    };

    // Obtain article information
    getArticle(this.state.url).then(res => {
      this.setState({
        title: res.data.article_title,
        article_text: res.data.article_content,
        article_reliability_score: res.data.article_reliability,
        article_paragraphs: res.data.article_paragraphs,
        citation_links: res.data.citation_links
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

    // Obtain publisher information
    getPublisher(this.state.url).then(res => {
      this.setState({
        publisher_name: res.data.publisher_name,
        publisher_introduction: res.data.publisher_introduction
      });
    });

    // Obtain citation information
    getCitationInformation(this.state.url).then(res => {
      this.setState({
        citation_information: res.data
      });
    });
  }

  renderTime = value => {
    if (value === 0) {
      return <div className="timer">done...</div>;
    }

    return (
      <div className="timer">
        <div className="text">Remaining</div>
        <div className="value">{value}</div>
        <div className="text">seconds</div>
      </div>
    );
  };

  // Render article page
  renderArticlePage = () => {
    if (this.state.recievedResponse) {
      return (
        <Redirect
          to={{
            pathname: "/article",
            state: {
              url: this.state.url,
              title: this.state.title,
              article_text: this.state.article_text,
              article_reliability_score: this.state.article_reliability_score,
              article_paragraphs: this.state.article_paragraphs,
              citation_links: this.state.citation_links,
              citation_information: this.state.citation_information,
              author_name: this.state.author_name,
              author_introduction: this.state.author_introduction,
              author_reliability_score: this.state.author_reliability_score,
              publisher_name: this.state.publisher_name,
              publisher_introduction: this.state.publisher_introduction
            }
          }}
        />
      );
    }
  };

  render() {
    return (
      <div className="loading">
        {this.renderArticlePage()}
        <div id="loading-logo">
          <img src={InfoRootsLogo} id="logo" alt="InfoRoots Logo" />
        </div>
        <h1>
          Your result is almost there…
          <br />
        </h1>
        <CountdownCircleTimer
          isPlaying
          durationSeconds={10}
          colors={[["#515151", 10]]}
          renderTime={this.renderTime}
          onComplete={() => {
            this.setState({ recievedResponse: true });
            return [true, 1000];
          }}
        />
        <p className="info"></p>
      </div>
    );
  }
}

export default LoadingPage;
