
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

function revealMeta(element) {
    element.querySelector(".meta").style.display = "block"
}

function hideMeta(element) {
    element.querySelector(".meta").style.display = "none"
}

const suggestions = document.getElementsByClassName("suggestion")

Array.from(suggestions).forEach((element, index) => {
    element.addEventListener("mouseenter", () => {
        revealMeta(element);
    })
    element.addEventListener("mouseleave", () => {
        hideMeta(element);
    })
});
