
import {useState} from 'react'
import {Switch, Route, Redirect} from 'react-router-dom'

import Header from './Header.js';
import Main from './pages/Main.js';
import About from './pages/About.js';
import Settings from './pages/Settings.js';

import useLocalStorage from './utils/use-local-storage.js';

import './App.css';

const baseUrl = process.env.REACT_APP_API_BASE_URL

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
    const [hskLevel, setHskLevel] = useLocalStorage("hskLevel", 4)
    const [usePinyinAccents, setUsePinyinAccents] = useLocalStorage("usePinyinAccents", false)

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
                    <Settings 
                        hskLevel={hskLevel} 
                        setHskLevel={setHskLevel}
                        usePinyinAccents={usePinyinAccents}
                        setUsePinyinAccents={setUsePinyinAccents}
                    /> 
                </Route>
                <Route path="/word/:word">
                    <Main hskLevel={hskLevel} usePinyinAccents={usePinyinAccents}/>
                </Route>

            </Switch>
        </div>
    )
}

export default App;
