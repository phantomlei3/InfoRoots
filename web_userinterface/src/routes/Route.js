import React from "react";
import { Route } from "react-router-dom";

export default function RouteWrapper({
  component: Component,
  articleUrl,
  ...rest
}) {
  return <Route {...rest} component={Component} />;
}
