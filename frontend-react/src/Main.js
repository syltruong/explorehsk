import {useState} from 'react'
import './Main.css'

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

function Center() {

    const [word, setWord] = useState(exampleWord)
    
    return (
        <div id={'center-container'}>
            <div id={'center-word'} className={'zh'}>{word.word}</div>
            <div className={'en meta'}>
                <div>{word.pronunciation}</div>
                <div>{word.translation}</div>
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


function Suggestions() {

    const [words, setWords] = useState(exampleSuggestions)

    const wordComponents = words.map(
        word => (
            <Suggestion 
                word={word.word} 
                pronunciation={word.pronunciation} 
                translation={word.translation}
            />
            )
    )

    return (
        <div id={"suggestions-container"}>
            {wordComponents}
        </div>
    )

}



function Main() {
    return (
        <main>
            <Center />
            <Suggestions />
        </main>
    )
}

export default Main