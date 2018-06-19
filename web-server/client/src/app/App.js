import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.min.js';

import React, { Component } from 'react';
import newslogo from '../newslogo.png';
import './App.css';

//import news panel
import NewsPanel from '../NewsPanel/NewsPanel';

class App extends React.Component{
    render() {
        return(
            <div>
                <img className='newslogo' src={newslogo} alt='newslogo'/>
                <div className='container'>
                    <NewsPanel />
                </div>
            </div>
        );
    }
}

export default App;

