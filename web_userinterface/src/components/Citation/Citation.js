import React from "react";
import "./Citation.css";

function Citation(props) {
  // No link
  if (props.link === "None") {
    return <span id="no-citation">{props.paragraph}</span>;
  } else {
    return (
      <span id="citation">
        <a id="link" href={props.link} target="_blank">
          {props.paragraph}
        </a>
      </span>
    );
  }
}

export default Citation;
