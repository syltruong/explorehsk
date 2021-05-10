// import './About.css'

import {useHistory} from 'react-router-dom'

function Settings(props) {
    
    const {hskLevel, setHskLevel, usePinyinAccents, setUsePinyinAccents} = props
   
    const onChangeHskLevel = event => {
        setHskLevel(event.target.value)
    }

    const onChangeUsePinyinAccents = event => {
        setUsePinyinAccents(event.target.checked)
    }

    let history = useHistory();

    return (
        <section className={"en"}>
            <h2>Settings</h2>
            <form>
                <label for="hsk-level-slider">
                    HSK Level <span id="hsk-level-span">{hskLevel}</span>
                </label>
                <input 
                    type="range" 
                    min="1" 
                    max="6" 
                    value={hskLevel}
                    name="hsk-level-slider" 
                    onChange={onChangeHskLevel}
                />
                
                <label for="use-pinyin-accents-checkbox">
                    Use pīnyīn accents
                </label>
                <input 
                    type="checkbox" 
                    id="use-pinyin-accents-checkbox" 
                    name="use-pinyin-accents-checkbox" 
                    onChange={onChangeUsePinyinAccents}
                    defaultChecked={usePinyinAccents}
                />
            </form>
            
            <button onClick={() => {history.goBack()}}> back </button>
        </section>
    )
}

export default Settings