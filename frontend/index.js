// Command handling

//// Coming soon

const btns = document.getElementsByClassName("comingSoon")
const settingsBtn = document.getElementById("settingsBtn")
const aboutBtn = document.getElementById("aboutBtn")
const comingSoonOverlayDiv = document.getElementById("coming-soon-overlay")
const settingsOverlayDiv = document.getElementById("settings-overlay")
const aboutOverlayDiv = document.getElementById("about-overlay")

function toggleHidden(elt){
    elt.classList.toggle("hidden")        
}

Array.from(btns).forEach(elt => {
    elt.addEventListener("click", () => toggleHidden(comingSoonOverlayDiv))
});
settingsBtn.addEventListener("click", () => toggleHidden(settingsOverlayDiv))
aboutBtn.addEventListener("click", () => toggleHidden(aboutOverlayDiv))
Array.from(document.getElementsByClassName("overlay")).forEach(
    elt => elt.addEventListener("click", () => toggleHidden(elt))
);

const hskLevelSlider = document.getElementById('hsk-level-slider')
function renderHskLevel() {
    document.getElementById("hsk-level-span").innerText = hskLevelSlider.value
}
hskLevelSlider.addEventListener("click", event => {
    event.stopPropagation();
})
hskLevelSlider.addEventListener("input", renderHskLevel)


// Display suggestions

function toggleMeta(elt) {  
    elt.querySelector(".meta").classList.toggle("hidden-meta")
}

function makeSuggestionsHoverable() {
    const suggestions = document.getElementsByClassName("suggestion")
    
    Array.from(suggestions).forEach(elt => {
        elt.querySelector(".suggestion__word").addEventListener("mouseenter", () => toggleMeta(elt))
        elt.querySelector(".suggestion__word").addEventListener("mouseleave", () => toggleMeta(elt))
    });
}

function makeSuggestionsClickable() {
    const suggestionWords = document.getElementsByClassName("suggestion__word")

    Array.from(suggestionWords).forEach(elt => {
        const word = elt.innerText;
        elt.addEventListener("click", () => populateFrom(word))
    });    
}

async function populateFrom(word) {
    try {
        const response = await fetch(baseUrl + `query?word=${word}&hskLevel=${hskLevelSlider.value}`);
        const jsonData = await response.json();

        populateCenter(jsonData.source)
        populateSuggestions(jsonData.most_similar)
        resetSuggestionScroller()

    } catch(err) {
        console.log(err)
    }
}

function resetSuggestionScroller() {
    document.getElementById("suggestion-container").scrollTop = 0
    document.getElementById("suggestion-container").scrollLeft = 0
}




//// Random

const randomBtn = document.getElementById("randomBtn")
const baseUrl = "http://explorehsk.com:5000/" 

randomBtn.addEventListener("click", () => {
    getRandomWord()
})

async function getRandomWord() {
    try {
        const response = await fetch(baseUrl + `random?hskLevel=${hskLevelSlider.value}`);
        const jsonData = await response.json();

        populateCenter(jsonData.source)
        populateSuggestions(jsonData.most_similar)
        resetSuggestionScroller()

    } catch(err) {
        console.log(err)
    }
}

function populateCenter(source) {
    const centerDiv = document.getElementById("center")
    centerDiv.querySelector(".center__word").innerHTML = source["Word"]
    centerDiv.querySelector(".pinyin").innerText = source["Pronunciation"]
    centerDiv.querySelector(".translation").innerText = source["Definition"]
}

function populateSuggestions(mostSimilar) {
    const suggestionContainerDiv = document.getElementById("suggestion-container") 
    
    // reset content
    suggestionContainerDiv.textContent = ""

    // populate with suggestions
    // we skip the first element on purpose
    // since it is the same as source
    for (let i=1; i<mostSimilar.length; i++){
        const item = mostSimilar[i]

        const suggestionDiv = document.createElement("div")
        suggestionDiv.classList.add("suggestion")

        const wordDiv = document.createElement("div")
        wordDiv.classList.add("zh")
        wordDiv.classList.add("suggestion__word")
        wordDiv.innerText = item["Word"]

        const metaDiv = document.createElement("div")
        metaDiv.classList.add("meta") 
        metaDiv.classList.add("hidden-meta")

        const pinyinDiv = document.createElement("div")
        pinyinDiv.classList.add("en") 
        pinyinDiv.classList.add("pinyin")
        pinyinDiv.innerText = item["Pronunciation"]

        const translationDiv = document.createElement("div")
        translationDiv.classList.add("en") 
        translationDiv.classList.add("translation")
        translationDiv.innerText = item["Definition"]

        metaDiv.appendChild(pinyinDiv)
        metaDiv.appendChild(translationDiv)
        suggestionDiv.appendChild(metaDiv)
        suggestionDiv.appendChild(wordDiv)

        suggestionContainerDiv.appendChild(suggestionDiv)

    }

    makeSuggestionsHoverable()
    makeSuggestionsClickable()
}

// rendering

// function setMainHeight() {
//     if (window.innerWidth < 972){
//         mainElt = document.querySelector("main")
//         mainElt.style.height = `calc(100vh - ${mainElt.offsetTop}px)`
//     }
// }

// window.addEventListener("resize", setMainHeight)

getRandomWord()
// setMainHeight()
renderHskLevel()
makeSuggestionsHoverable()
makeSuggestionsClickable()