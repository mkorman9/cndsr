import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import './index.css';
import Home from './components/Home';
import About from './components/About';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(
    <BrowserRouter>
        <Switch>
            <Route path="/about" component={About}/>
            <Route path="/" component={Home}/>
        </Switch>
    </BrowserRouter>,
    document.getElementById('root')
);

registerServiceWorker();
