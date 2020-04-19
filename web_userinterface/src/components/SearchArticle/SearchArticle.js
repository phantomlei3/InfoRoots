import React from "react";
import "./SearchArticle.css";
import Rater from "react-rater";
import "react-rater/lib/react-rater.css";
import { CircleArrow as ScrollUpButton } from "react-scroll-up-button";
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
      citation_information: this.props.location.state.citation_information,
      author_name: this.props.location.state.author_name,
      author_introduction: this.props.location.state.author_introduction,
      author_reliability_score: this.props.location.state
        .author_reliability_score,
      author_link: this.props.location.state.author_link,
      publisher_name: this.props.location.state.publisher_name,
      publisher_introduction: this.props.location.state.publisher_introduction,
      publisher_reliability_score: this.props.location.state
        .publisher_reliability_score,
      publisher_link: this.props.location.state.publisher_link,
      authorCardToggled: false,
      publisherCardToggled: false,
      citationDisplayed: false,
      borderClass: "border",
      citationClass: "citation-container",
      citationLink: "",
      citationTitle: "",
      citationContent: "",
      citationCredibility: "",
      currArrowLink: "None"
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

  // Function to handle rndering a citation's information
  setCitationLink = link => {
    if (this.state.citationDisplayed === true) {
      if (this.state.citationLink === link) {
        this.setState({
          citationDisplayed: false,
          citationLink: "",
          borderClass: "border-inactive",
          citationClass: "citation-container-inactive",
          currArrowLink: "None"
        });
      } else {
        this.setState({
          citationLink: link,
          citationDisplayed: true,
          borderClass: "border-active",
          citationClass: "citation-container-active",
          citationTitle: this.state.citation_information[link].article_title,
          citationContent: this.state.citation_information[link]
            .article_content,
          citationCredibility: this.state.citation_information[link]
            .article_credibility,
          currArrowLink: link
        });
      }
    } else {
      this.setState({
        citationLink: link,
        citationDisplayed: true,
        borderClass: "border-active",
        citationClass: "citation-container-active",
        citationTitle: this.state.citation_information[link].article_title,
        citationContent: this.state.citation_information[link].article_content,
        citationCredibility: this.state.citation_information[link]
          .article_credibility,
        currArrowLink: link
      });
    }
  };

  // Function to handle citations in the article text
  renderArticleText = () => {
    var elements = [];
    for (let i = 0; i < this.state.article_paragraphs.length; i++) {
      if (this.state.citation_links[i] !== "None") {
        elements.push(
          <Citation
            key={i}
            link={this.state.citation_links[i]}
            paragraph={this.state.article_paragraphs[i].substr(
              0,
              this.state.article_paragraphs[i].length
            )}
            citation_information={
              this.state.citation_information[this.state.citation_links[i]]
            }
            setCitationLink={this.setCitationLink.bind(this)}
            currArrowLink={this.state.currArrowLink}
          />
        );
      } else {
        elements.push(
          <Citation
            key={i}
            link={this.state.citation_links[i]}
            paragraph={this.state.article_paragraphs[i].substr(
              0,
              this.state.article_paragraphs[i].length
            )}
            currArrowLink="None"
          />
        );
      }

      if (i < this.state.article_paragraphs.length - 1) {
        elements.push(<p key={9999 - i}></p>);
        elements.push(<p key={999 - i}></p>);
        elements.push(<br key={99 - i}></br>);
      }
    }

    return elements;
  };

  render() {
    let articleText = this.renderArticleText();
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
                  author_link={this.state.author_link}
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
                  publisher_reliability_score={
                    this.state.publisher_reliability_score
                  }
                  publisher_link={this.state.publisher_link}
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
          {[
            <div key="border" id={this.state.borderClass} />,
            <div key="citation" id={this.state.citationClass}>
              {this.state.citationDisplayed && [
                <div id="citation-title" key="citation-title">
                  {this.state.citationTitle}
                </div>,
                <div id="citation-rating" key="citation-rating">
                  Rating:{" "}
                  <Rater
                    total={5}
                    interactive={false}
                    rating={this.state.citationCredibility * 5}
                  />
                </div>,
                <div id="citation-content" key="citation-content">
                  {this.state.citationContent.substr(0, 600) + "..."}
                </div>,
                <div id="citation-readmore" key="citation-readmore">
                  <a
                    id="citation-button"
                    href={this.state.citationLink}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Read more >
                  </a>
                </div>
              ]}
            </div>
          ]}
        </div>
        <div id="bottom-header">InfoRoots, Spring 2020 {"\u00A9"}</div>
        <ScrollUpButton />
      </div>
    );
  }
}

export default SearchArticle;
