import './Settings.css'

import {useHistory} from 'react-router-dom'

function Settings(props) {
    
    const {hskLevel, setHskLevel, usePinyinAccents, setUsePinyinAccents} = props

    const onChangeHskLevel = event => {
        setHskLevel(parseInt(event.target.value))
    }

    const onChangeUsePinyinAccents = event => {
        setUsePinyinAccents(event.target.value === "true")
    }

    let history = useHistory();

    const hskLevels = []

    for (let i=1; i<8; i++) {
        hskLevels.push(
            <div>
                <input 
                    id={`hsk${i}`} 
                    type="radio" 
                    name="hskLevel" 
                    checked={hskLevel === i} 
                    value={i}
                    onChange={onChangeHskLevel}
                />
                <label htmlFor={`hsk${i}`}>{i}</label>
            </div>
        )
    }

    return (
        <section className={"en"}>
            <h2>Settings</h2>
            <form>

                <div className="setting">
                    <label>HSK Level</label>
                    <div id="hskLevels">
                        {hskLevels}
                    </div>
                </div>
                
                <div className="setting">
                    <label>Use {(usePinyinAccents) ? "pīnyīn" : "pinyin"} accents</label>
                    <div>
                        <input 
                            id={"usePinyinAccentsTrue"} 
                            type="radio" 
                            name="usePinyinAccents" 
                            value={true}
                            checked={usePinyinAccents} 
                            onChange={onChangeUsePinyinAccents}
                        />
                        <label htmlFor={"usePinyinAccentsTrue"}>yes</label>
                        <input 
                            id={"usePinyinAccentsFalse"}  
                            type="radio" 
                            name="usePinyinAccents" 
                            value={false}
                            checked={!(usePinyinAccents)}
                            onChange={onChangeUsePinyinAccents}
                        />
                        <label htmlFor={"usePinyinAccentsFalse"}>no</label>
                    </div>
                </div>
            </form>
            
            <button onClick={() => {history.goBack()}}>&#60; back </button>
        </section>
    )
}

export default Settings