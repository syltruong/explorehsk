import {useState, useEffect} from 'react'

import Header from './Header.js';
import Main from './Main.js';

import './App.css';

const exampleWord = {
    word: "什么",
    pronunciation: "shen3 me5",
    translation: "what"
}

const numberSuggestions = 20

const exampleSuggestions = []

for (let i=0; i < numberSuggestions; i++) {
    exampleSuggestions.push(exampleWord)
}

const baseUrl = "http://explorehsk.com:5000/"

async function getRandomWord() {
    try {
        const response = await fetch(baseUrl + `random`);
        const jsonData = await response.json();

        return jsonData

    } catch(err) {
        console.log(err)
    }
}

function App() {

    const [centerWord, setCenterWord] = useState(exampleWord)
    const [suggestionWords, setSuggestionWords] = useState(exampleSuggestions)

    function populateRandom() {
        const jsonData = getRandomWord()        
        
        jsonData.then(value => {
            console.log(value)
            setCenterWord(value.source)
            setSuggestionWords(value.most_similar.slice(1)) 
        })
    }

    // componentDidMount
    useEffect(populateRandom, [])

    return (
        <div id="app-container">
            <Header onRandom={populateRandom}/>
            <Main centerWord={centerWord} suggestionWords={suggestionWords}/>
        </div>
    )
}

export default App;
