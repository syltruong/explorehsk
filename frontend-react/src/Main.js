import './Main.css'

function Center(props) {

    const {word} = props;
    
    return (
        <div id={'center-container'}>
            <div id={'center-word'} className={'zh'}>{word.Word}</div>
            <div className={'en meta'}>
                <div>{word.Pronunciation}</div>
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

    const {words} = props

    const wordComponents = words.map(
        word => (
            <Suggestion 
                word={word.Word} 
                pronunciation={word.Pronunciation} 
                translation={word.Definition}
                // key={word.word + word.pronunciation} 
                // TODO: set a unique key, will likely come from the backend
            />
            )
    )

    return (
        <div id={"suggestions-container"}>
            {wordComponents}
        </div>
    )

}



function Main(props) {

    const {centerWord, suggestionWords} = props

    return (
        <main>
            <Center word={centerWord} />
            <Suggestions words={suggestionWords} />
        </main>
    )
}

export default Main