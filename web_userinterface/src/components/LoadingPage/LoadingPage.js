import React from "react";
import ReactDOM from "react-dom";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Redirect } from "react-router-dom";
import { getArticle, getAuthor, getPublisher } from "../../api.js";
import "./LoadingPage.css";

class LoadingPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: props.location.state.url,
      title: "",
      author: "",
      publisher: "",
      articleText: "",
      author_name: "",
      author_introduction: "",
      author_reliability_score: 0,
      publisher_name: "",
      publisher_introduction: "",
      recievedResponse: false
    };

    // Obtain article information
    getArticle(this.state.url).then(res => {
      this.setState({
        title: res.data.article_title,
        articleText: res.data.article_content
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
              articleText: this.state.articleText,
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
