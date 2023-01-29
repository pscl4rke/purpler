function triggerFakeEvent() {
    let message = "Hello World " + Math.floor(Math.random() * 100);
    handleEvent(message);
}

function startFollowingEvents() {
    console.log("Connecting to '/events'");
    const eventSource = new EventSource("/events");
    eventSource.addEventListener("newnumber", (event) => {
        let message = "Hello from Server " + event.data;
        handleEvent(message);
    })
    eventSource.onerror = (err) => {
        console.log("Event Source Error Here " + err);
        startFollowingEvents();
    }
}

function handleEvent(message) {
    let node = document.createElement("p");
    node.innerHTML = feather.icons["arrow-right-circle"].toSvg() + message;
    document.body.appendChild(node);
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("I have loaded!");
    //setInterval(triggerFakeEvent, 2000);
    startFollowingEvents();
});
