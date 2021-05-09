
import {useState} from 'react'
import {Switch, Route, Redirect} from 'react-router-dom'

import Header from './Header.js';
import Main from './Main.js';
import About from './About.js';
import Settings from './Settings.js';

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
    const [hskLevel, setHskLevel] = useState(4)  // TODO: get this to be set with cookie

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
                <Route exact path="/settings">
                    <Settings hskLevel={hskLevel} setHskLevel={setHskLevel}/> 
                </Route>
                <Route path="/word/:word">
                    <Main hskLevel={hskLevel} />
                </Route>

            </Switch>
        </div>
    )
}

export default App;
