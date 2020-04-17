import React from "react";
import "./Citation.css";

function Citation(props) {
  // No link
  if (props.link === "None") {
    return <div id="no-citation">{props.paragraph}</div>;
  } else {
    return (
      <div id="citation">
        <a id="link" href={props.link} target="_blank">
          {props.paragraph}
        </a>
      </div>
    );
  }
}

export default Citation;
