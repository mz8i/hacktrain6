import React from 'react';
import { Link } from 'react-router-dom';

import './Home.css';

class Home extends React.Component {
  render() {
    return (

      <div className="Home">
        {/* <Jumbotron> */}
          <h1>Team Magic</h1>
        {/* </Jumbotron> */}
        <Link to="/map">Map</Link>
      </div>
    );
  }
}

export default Home;
