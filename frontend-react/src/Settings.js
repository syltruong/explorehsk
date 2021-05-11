import './Settings.css'

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

    const hskLevels = []

    for (let i=1; i<7; i++) {
        hskLevels.push(
            <div>
                <input id={`hsk${i}`} type="radio" name="hskLevel"/><label for={`hsk${i}`}>{i}</label>
            </div>
        )
    }

    return (
        <section className={"en"}>
            <h2>Settings</h2>
            <form>

                <div className="setting">
                    <label for="hsk-level-slider">
                        HSK Level <span id="hsk-level-span">{hskLevel}</span>
                    </label>
                    <input 
                        type="range" 
                        min="1" 
                        max="6" 
                        value={hskLevel}
                        name="hsk-level-slider" 
                        id="hsk-level-slider"  
                        onChange={onChangeHskLevel}
                    />
                </div>

                <div className="setting">
                    <label>HSK Level</label>
                    <div id="hskLevels">
                        {hskLevels}
                    </div>
                </div>
                
                <div className="setting">
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
                </div>
            </form>
            
            <button onClick={() => {history.goBack()}}>&#60; back </button>
        </section>
    )
}

export default Settings