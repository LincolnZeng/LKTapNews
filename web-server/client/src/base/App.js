import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.min.js';


import React, { Component } from 'react';
import newslogo from '../newslogo.png';
import './App.css';

//import news panel
import NewsPanel from '../NewsPanel/NewsPanel';

class App extends Component {
    render() {
        return (
            <div className="App">
            <img className="newslogo" src={newslogo} alt='logo'/>
            <div className="container">
            <NewsPanel/>
            </div>
            </div>
    );
    }
}

export default App;
