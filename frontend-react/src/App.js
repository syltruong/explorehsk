
import {useState} from 'react'
import {Switch, Route, Redirect} from 'react-router-dom'

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

    const [randomWord, setRandomWord] = useState("什么")

    return (
        <div id="app-container">
            <Header />
            <Switch>
                <Redirect exact from="/" to="/random" />
                <Route 
                    exact 
                    path="/random"
                    render={
                        () => {
                            const jsonData = getRandomWord()
                            jsonData.then(value => {
                                setRandomWord(value.source.Word)
                            })

                            return <Redirect to={`/word/${randomWord}`}/>
                        }
                    }
                />
                 
                <Route exact path="/about" component={About} />
                <Route path="/word/:word" component={Main} />

            </Switch>
        </div>
    )
}

export default App;
