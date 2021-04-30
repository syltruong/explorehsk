import {useState, useEffect} from 'react'
import {Switch, Route} from 'react-router-dom'

import Header from './Header.js';
import Main from './Main.js';
import About from './About.js';

import './App.css';

const baseUrl = "http://explorehsk.com:5000/"

async function getRandomWord() {
    try {
        const response = await fetch(baseUrl + `random`);
        const jsonData = await response.json();

        return jsonData;

    } catch(err) {
        console.log(err)
    }
}


function App() {

    return (
        <div id="app-container">
            <Header />
            <Switch>
                {/* <Route exact path="/">
                    <Main 
                        centerWord={centerWord} 
                        suggestionWords={suggestionWords} 
                        onWordClick={populateFromWord}
                    />
                </Route> */}
                <Route exact path="/about">
                    <About />
                </Route>
                <Route path="/word/:word">
                    <Main />
                </Route>
            </Switch>
        </div>
    )
}

export default App;
