import React from "react";
import { Switch } from "react-router-dom";
import Route from "./Route";

import Homepage from "../components/Homepage/Homepage.js";
import SearchArticle from "../components/SearchArticle/SearchArticle.js";

export default function Routes() {
  return (
    <Switch>
      <Route path="/" exact component={Homepage} />
      <Route path="/article/:articleUrl" component={SearchArticle} />
      <Route component={Homepage} />
    </Switch>
  );
}
