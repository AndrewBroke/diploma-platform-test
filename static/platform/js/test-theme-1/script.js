let app
console.log(static_url)
window.onload = function () {
    app = new PIXI.Application({
        width: 800,
        height: 600,
        backgroundColor: 0xAAAAAA
    })

    let main = document.querySelector("main")
    main.appendChild(app.view)

    sprite = PIXI.Sprite.from(static_url + "platform/img/test-theme-1/sample.png")
    app.stage.addChild(sprite)
    sprite.interactive = true
    sprite.on("pointerdown", (event) => {
        alert("clicked!")
    })

    let elapsed = 0.0;
    app.ticker.add((delta) => {
        elapsed += delta;
        sprite.x = 100.0 + Math.cos(elapsed / 50.0) * 100.0;
    });
}