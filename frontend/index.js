// Display suggestions

function toggleMeta(elt) {  
    elt.querySelector(".meta").classList.toggle("hidden")
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
        const response = await fetch(baseUrl + "query?word=" + word);
        const jsonData = await response.json();

        console.log(jsonData)
        populateCenter(jsonData.source)
        populateSuggestions(jsonData.most_similar)

    } catch(err) {
        console.log(err)
    }
}


// Command handling

//// Coming soon

const btns = document.getElementsByClassName("comingSoon")
const overlayDiv = document.getElementById("overlay")

function toggleOverlay(){
    overlayDiv.classList.toggle("hidden")        
}

Array.from(btns).forEach(elt => {
    elt.addEventListener("click", toggleOverlay)
});
overlayDiv.addEventListener("click", toggleOverlay)

//// Random

const randomBtn = document.getElementById("randomBtn")
const baseUrl = "http://0.0.0.0:5000/" 

randomBtn.addEventListener("click", () => {
    console.log("click")
    getRandomWord()
})

async function getRandomWord() {
    try {
        const response = await fetch(baseUrl + "random");
        const jsonData = await response.json();

        console.log(jsonData)
        populateCenter(jsonData.source)
        populateSuggestions(jsonData.most_similar)

    } catch(err) {
        console.log(err)
    }
}

function populateCenter(source) {
    centerDiv = document.getElementById("center")
    centerDiv.querySelector(".center__word").innerText = source["Word"]
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
        metaDiv.classList.add("hidden")

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

getRandomWord()