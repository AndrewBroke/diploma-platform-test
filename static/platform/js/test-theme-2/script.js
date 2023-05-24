console.log("Load script for test theme 2")

let violationBtn = document.querySelector("#violation-btn")
let noViolationBtn = document.querySelector("#no-integrity-btn")
let clearBtn = document.querySelector("#clear-btn")
let measures = document.querySelectorAll("select[name^='question-measure']")
console.log(measures)

let canClickStamp = true

function getActiveSlide(){
    return document.querySelector("#carouselQuestions .carousel-inner .active")
}

function clearStamp(){
    if(!canClickStamp) return

    let activeSlide = getActiveSlide()
    let stamps = activeSlide.querySelectorAll(".question-stamps img")
    stamps.forEach(element => {
        element.style.display = "none"
    });
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "-1")
}

function showViolationStamp(){
    if(!canClickStamp) return
    clearStamp()
    let activeSlide = getActiveSlide()
    let violationStamp = activeSlide.querySelector("#question-violation")
    violationStamp.style.display = "block"
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "4")
}

function showNoViolationStamp(){
    if(!canClickStamp) return
    clearStamp()
    let activeSlide = getActiveSlide()
    let violationStamp = activeSlide.querySelector("#question-no-violation")
    violationStamp.style.display = "block"
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "5")
}

clearBtn.addEventListener("click", clearStamp)
violationBtn.addEventListener("click", showViolationStamp)
noViolationBtn.addEventListener("click", showNoViolationStamp)



let carousel = document.querySelector("#carouselQuestions")
carousel.addEventListener("slide.bs.carousel", () => {
    canClickStamp = false
})

carousel.addEventListener("slid.bs.carousel", () => {
    canClickStamp = true
    let currentSlide = getActiveSlide()
    let currentQuestion = currentSlide.querySelector("input").getAttribute("name").split("-").at(-1)
    clearMeasures()
    setActiveMeasure(currentQuestion)
    console.log(currentQuestion)
})

function setActiveMeasure(question){
    measures.forEach(element => {
        if(element.getAttribute("name").split("-").at(-1) == question){
            element.style.display = "block"
        }
    });
}

function clearMeasures(){
    measures.forEach(element => {
        element.style.display = "none"
    });
}

function sendTestCallback(event){
    let inputs = document.querySelectorAll("input[name]")
    for (let i = 0; i < inputs.length; i++) {
        if(inputs[i].value == "-1"){
            event.preventDefault()
            alert("Не все ответы заполнены")
            return
        }
    }
}

let sendBtn = document.querySelector("[type='submit']")
sendBtn.addEventListener("click", sendTestCallback)