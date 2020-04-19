import axios from "axios";
import React from "react";
import { Redirect } from "react-router-dom";

// Request for processing a user's search query
export async function processUserSearch(searchQuery) {
  var search = "/searchArticle/&url=" + encodeURIComponent(searchQuery);
  let searchQueryRes = await axios.get(search);
  return searchQueryRes;
}

// Request for recieving article information
export async function getArticle(url) {
  let res = await axios.get("/getArticle");
  return res;
}

// Request for recieving author information
export async function getAuthor(url) {
  let res = await axios.get("/getAuthorCard");
  return res;
}

// Request for recieving publisher information
export async function getPublisher(url) {
  let res = await axios.get("/getPublisherCard");
  return res;
}

// Request for recieving citation information
export async function getCitationInformation(url) {
  let res = await axios.get("/getCitationInformation");
  return res;
}

// Function to handle searching of a URL on the homepage
export function handleSearch() {
  if (this.state.searchQuery.length === 0) {
    return;
  }

  processUserSearch(this.state.searchQuery).then(res => {
    if (res.data === "Okey") {
      this.setState({ articleSearched: true });
    }
  });
}

// Render article page
export function renderArticlePage() {
  if (this.state.articleSearched) {
    return (
      <Redirect
        to={{
          pathname: "/loading",
          state: { url: encodeURIComponent(this.state.searchQuery) }
        }}
      />
    );
  }
}

export function setSearchQuery(event) {
  this.setState({
    searchQuery: event.target.value
  });
}

// Handle when the user presses enter to search
export function enterPressed(event) {
  var code = event.which;
  if (code === 13) {
    this.handleSearch();
  }
}
