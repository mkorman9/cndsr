import React, { Component } from 'react';
import '../index.css';
import { Link } from 'react-router-dom'

class Home extends Component {
  render() {
    return (
      <div className="Main">
        <header className="Main-header">
          <h1 className="Main-title">cndsr</h1>
        </header>
        <p className="Main-intro">
            Homepage
            <p><Link to="/about">About</Link></p>
        </p>
      </div>
    );
  }
}

export default Home;
