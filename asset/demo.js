function triggerFakeEvent() {
    let message = "Hello World " + Math.floor(Math.random() * 100);
    handleEvent(message);
}

function handleEvent(message) {
    let node = document.createElement("p");
    node.innerHTML = feather.icons["arrow-right-circle"].toSvg() + message;
    document.body.appendChild(node);
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("I have loaded!");
    setInterval(triggerFakeEvent, 2000);
});
