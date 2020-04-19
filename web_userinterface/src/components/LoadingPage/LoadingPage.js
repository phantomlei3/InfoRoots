import React from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Redirect } from "react-router-dom";
import { processUserSearch, getArticleInformation } from "../../api.js";
import "./LoadingPage.css";
import InfoRootsLogo from "../../static/logo.png";

class LoadingPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: decodeURIComponent(props.location.state.url),
      title: "",
      article_text: "",
      article_reliability_score: "",
      author_name: "",
      author_introduction: "",
      author_reliability_score: 0,
      author_link: "",
      publisher_name: "",
      publisher_introduction: "",
      publisher_link: "",
      article_paragraphs: [],
      citation_links: [],
      citation_information: [],
      validSearch: 0,
      errorMessage: false,
      redirect: false
    };
  }

  renderTime = value => {
    return (
      <div className="timer">
        <div className="value">Loading...</div>
      </div>
    );
  };

  redirectHandler = () => {
    if (this.state.validSearch === 1 && this.state.redirect === true) {
      return this.renderArticlePage();
    } else if (this.state.validSearch === 2 && this.state.redirect === true) {
      return this.renderHomePage();
    }
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
              author_link: this.state.author_link,
              publisher_name: this.state.publisher_name,
              publisher_introduction: this.state.publisher_introduction,
              publisher_reliability_score: this.state
                .publisher_reliability_score,
              publisher_link: this.state.publisher_link
            }
          }}
        />
      );
    }
  };

  // Render home page
  renderHomePage = () => {
    return <Redirect to={{ pathname: "/" }} />;
  };

  componentDidMount() {
    processUserSearch.call(this, this.state.url).then(res => {
      if (res.data === "Failed") {
        this.setState({ validSearch: 2, errorMessage: true });
      } else if (res.data === "Okey") {
        getArticleInformation.call(this).then(res => {
          this.setState({ validSearch: 1 });
        });
      }
    });
  }

  render() {
    return (
      <div className="loading">
        {this.redirectHandler()}
        <div id="loading-logo">
          <img src={InfoRootsLogo} id="logo" alt="InfoRoots Logo" />
        </div>
        <h1>
          Your result is almost there…
          <br />
        </h1>
        <CountdownCircleTimer
          isPlaying
          durationSeconds={5}
          colors={[["#515151", 10]]}
          renderTime={this.renderTime}
          onComplete={() => {
            this.setState({ redirect: true });
            return [true, 0];
          }}
        />
        {this.state.errorMessage && (
          <div id="error-message">
            <div id="sorry">
              Sorry, our system cannot recognize and process the given URL
            </div>
            <div id="return"> Returning to home... </div>
          </div>
        )}
      </div>
    );
  }
}

export default LoadingPage;
