
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
