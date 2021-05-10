import './Main.css'

import {useParams, Link} from 'react-router-dom'
import {useState, useEffect} from 'react'

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

async function getSuggestions(word, hskLevel=4) {
    try {
        const response = await fetch(baseUrl + `query?word=${word}&hskLevel=${hskLevel}`);
        const jsonData = await response.json();

        return jsonData;

    } catch(err) {
        console.log(err)
    }
}

function getPronunciation(word, usePinyinAccents) {
    return (usePinyinAccents) ? word.Pronunciation_with_accents : word.Pronunciation
}

function Center(props) {

    const {word, usePinyinAccents} = props;
    
    return (
        <div id={'center-container'}>
            <div id={'center-word'} className={'zh'}>{word.Word}</div>
            <div className={'en meta'}>
                <div>{getPronunciation(word, usePinyinAccents)}</div>
                <div>{word.Definition}</div>
            </div>
        </div>
    )

}


function Suggestion(props) {
    const {word, pronunciation, translation} = props;

    return (
        <div className={"suggestion"}>
            <div className={'zh'}>{word}</div>
            <div className={'en meta'}>
                <div>{pronunciation}</div>
                <div>{translation}</div>
            </div>
        </div>
    )
}


function Suggestions(props) {

    const {words, usePinyinAccents} = props

    const wordComponents = words.map(
        word => (
            <Link to={`/word/${word.Word}`}>
                <Suggestion 
                    word={word.Word} 
                    pronunciation={getPronunciation(word, usePinyinAccents)} 
                    translation={word.Definition}
                    // key={word.word + word.pronunciation} 
                    // TODO: set a unique key, will likely come from the backend
                />
            </ Link>
            )
    )

    return (
        <div id={"suggestions-container"}>
            {wordComponents}
        </div>
    )

}


function Main(props) {

    const {word} = useParams()
    const {hskLevel, usePinyinAccents} = props

    const [centerWord, setCenterWord] = useState(exampleWord)
    const [suggestionWords, setSuggestionWords] = useState(exampleSuggestions)

    function populateFromWord() {
        const jsonData = getSuggestions(word, hskLevel)        
        
        jsonData.then(value => {
            setCenterWord(value.source)
            setSuggestionWords(value.most_similar.slice(1)) 
        })
    }

    useEffect(populateFromWord, [word, hskLevel])

    return (
        <main>
            <Center word={centerWord} usePinyinAccents={usePinyinAccents}/>
            <Suggestions words={suggestionWords} usePinyinAccents={usePinyinAccents}/>
        </main>
    )
}

export default Main