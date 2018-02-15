import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom'
import './index.css';
import Home from './components/Home';
import About from './components/About';
import GitHubForkRibbon from 'react-github-fork-ribbon';

ReactDOM.render(
    <BrowserRouter>
        <div className="Main">
            <header>
                <h1 className="Main-logo"><Link to="/">cndsr</Link></h1>
                <nav>
                    <ul>
                        <li><Link to="/about">About</Link></li>
                        <li><Link to="/">Shorten URL</Link></li>
                    </ul>
                </nav>

                <GitHubForkRibbon
                    href="//github.com/mkorman9/cndsr"
                    target="_blank"
                    position="right"
                    color="orange">
                    Fork me on GitHub
                </GitHubForkRibbon>
            </header>
            <div className="Main-intro">
                <Switch>
                    <Route exact path="/" component={Home}/>
                    <Route path="/about" component={About}/>
                </Switch>
            </div>
        </div>
    </BrowserRouter>
    ,
    document.getElementById('root')
);
