import React, { Component } from 'react';
import logo from './logo.svg';
import './Style.css';

class About extends Component {
  render() {
    return (
      <div className="Main">
        <header className="Main-header">
          <img src={logo} className="Main-logo" alt="logo" />
          <h1 className="Main-title">Welcome to React</h1>
        </header>
        <p className="Main-intro">
          About
        </p>
      </div>
    );
  }
}

export default About;
