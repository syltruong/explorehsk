
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
    } catch(err) {
        console.log(err)
    }
}


// Display suggestions

function toggleMeta(elt) {  
    elt.querySelector(".meta").classList.toggle("hidden")
}

const suggestions = document.getElementsByClassName("suggestion")

Array.from(suggestions).forEach(elt => {
    elt.addEventListener("mouseenter", () => toggleMeta(elt))
    elt.addEventListener("mouseleave", () => toggleMeta(elt))
});


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