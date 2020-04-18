import React from "react";
import "./Citation.css";

class Citation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      arrowDisplayed: false
    };
  }
  // Function to handle setting the link in the parent component
  setLink = () => {
    this.props.setCitationLink(this.props.link);
  };

  componentWillReceiveProps(newProps) {
    if (
      newProps.currArrowLink === newProps.link &&
      newProps.currArrowLink !== "None"
    ) {
      this.setState({
        arrowDisplayed: true
      });
    } else {
      this.setState({
        arrowDisplayed: false
      });
    }
  }

  // No link
  render() {
    return (
      <div>
        {this.state.arrowDisplayed && (
          <div id="arrow-container">
            <div id="arrow-left"></div>
          </div>
        )}
        {this.props.link === "None" ? (
          <div id="no-citation">{this.props.paragraph}</div>
        ) : (
          <div id="citation" onClick={this.setLink}>
            {this.props.paragraph}
          </div>
        )}
      </div>
    );
  }
}

export default Citation;
