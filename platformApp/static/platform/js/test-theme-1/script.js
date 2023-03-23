let integrityBtn = document.querySelector("#integrity-btn")
let privacyBtn = document.querySelector("#privacy-btn")
let accessBtn = document.querySelector("#access-btn")
let clearBtn = document.querySelector("#clear-btn")

let canClickStamp = true

function getActiveSlide(){
    return document.querySelector("#carouselQuestions .carousel-inner .active")
}

function showIntegrityStamp(){
    if(!canClickStamp) return
    clearStamp()
    let activeSlide = getActiveSlide()
    //activeSlide.querySelector(".question-stamps img").style.display = "none"
    let integrityStamp = activeSlide.querySelector("#question-integrity")
    integrityStamp.style.display = "block"
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "3")
}

function showPrivacyStamp(){
    if(!canClickStamp) return
    clearStamp()
    let activeSlide = getActiveSlide()
    //activeSlide.querySelector(".question-stamps img").style.display = "none"
    let privacyStamp = activeSlide.querySelector("#question-privacy")
    privacyStamp.style.display = "block"
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "2")
}

function showAccessStamp(){
    if(!canClickStamp) return
    clearStamp()
    let activeSlide = getActiveSlide()
    let accessStamp = activeSlide.querySelector("#question-access")
    accessStamp.style.display = "block"
    let input = activeSlide.querySelector("input")
    input.setAttribute("value", "1")
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

integrityBtn.addEventListener("click", showIntegrityStamp)
privacyBtn.addEventListener("click", showPrivacyStamp)
accessBtn.addEventListener("click", showAccessStamp)
clearBtn.addEventListener("click", clearStamp)

let carousel = document.querySelector("#carouselQuestions")
carousel.addEventListener("slide.bs.carousel", () => {
    canClickStamp = false
})

carousel.addEventListener("slid.bs.carousel", () => {
    canClickStamp = true
})

function sendTestCallback(event){
    let inputs = document.querySelectorAll("input[name]")
    return // Для теста!!!
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