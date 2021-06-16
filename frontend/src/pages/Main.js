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

const baseUrl = process.env.REACT_APP_API_BASE_URL

async function getSuggestions(wordId, hskLevel=4) {
    try {
        const response = await fetch(baseUrl + `query?wordId=${wordId}&hskLevel=${hskLevel}`);
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
                <div>[HSK {word.HSK_Level}] {word.Definition}</div>
            </div>
        </div>
    )

}


function Suggestion(props) {
    const {word, pronunciation, hskLevel, translation} = props;

    const [displayMeta, setDisplayMeta] = useState(false)

    return (
        <div 
            className={"suggestion"} 
            onMouseLeave={() => setDisplayMeta(false)}
        >
            <div 
                className={'zh'} 
                onMouseEnter={() => setDisplayMeta(true)}
            >
                {word}
            </div>
            
            <div 
                className={`en meta${displayMeta ? '' : ' hidden'}`}
            >
                <div className={'suggestion-pinyin'}>{pronunciation}</div>
                <div className={'suggestion-translation'}>[HSK {hskLevel}] {translation}</div>
            </div>
        </div>
    )
}


function Suggestions(props) {

    const {words, usePinyinAccents} = props

    const wordComponents = words.map(
        word => (
            <Link to={`/wordId/${word.Id}`}>
                <Suggestion 
                    word={word.Word} 
                    pronunciation={getPronunciation(word, usePinyinAccents)} 
                    hskLevel={word.HSK_Level}
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

    const {wordId} = useParams()
    const {hskLevel, usePinyinAccents} = props

    const [centerWord, setCenterWord] = useState(exampleWord)
    const [suggestionWords, setSuggestionWords] = useState(exampleSuggestions)

    function populateFromWord() {
        const jsonData = getSuggestions(wordId, hskLevel)        
        
        jsonData.then(value => {
            setCenterWord(value.source)
            setSuggestionWords(value.most_similar) 
        })
    }

    useEffect(populateFromWord, [wordId, hskLevel])

    return (
        <main>
            <Center word={centerWord} usePinyinAccents={usePinyinAccents}/>
            <Suggestions words={suggestionWords} usePinyinAccents={usePinyinAccents}/>
        </main>
    )
}

export default Main