import {useState} from 'react'

function Center() {

    const [word, setWord] = useState({
        word: "什么",
        pronunciation: "shen3me5",
        translation: "what"
    })
    
    return (
        <div>
            <div>{word.word}</div>
            <div>
                <div>{word.pronunciation}</div>
                <div>{word.translation}</div>
            </div>
        </div>
    )

}


function Suggestion(props) {
    const {word, pronunciation, translation} = props;

    return (
        <div>
            <div>{word}</div>
            <div>
                <div>{pronunciation}</div>
                <div>{translation}</div>
            </div>
        </div>
    )
}


function Suggestions() {

    const [words, setWords] = useState([
        {
            word: "什么",
            pronunciation: "shen3me5",
            translation: "what"
        },
        {
            word: "什么",
            pronunciation: "shen3me5",
            translation: "what"
        },
        {
            word: "什么",
            pronunciation: "shen3me5",
            translation: "what"
        }
    ])

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
        <div>
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