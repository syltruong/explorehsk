// import './About.css'

function Settings(props) {
    
    const {hskLevel, setHskLevel} = props
   
    const onChange = event => {
        setHskLevel(event.target.value)
    }

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
                    onChange={onChange}
                />
            </form>
        </section>
    )
}

export default Settings