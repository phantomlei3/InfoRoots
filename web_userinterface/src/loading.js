import React from "react";
import ReactDOM from "react-dom";
import { CountdownCircleTimer } from "react-countdown-circle-timer";

import "./styles.css";

const renderTime = value => {
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

function App() {
  return (
    <div className="App">
      <h1>
      Your result is almost there…
        <br />
        
      </h1>
      <CountdownCircleTimer
        isPlaying
        durationSeconds={10}
        colors={[["#515151", 10]]}
        renderTime={renderTime}
        onComplete={() => [true, 1000]}
      />
      <p className="info">

      </p>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
