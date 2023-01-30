
class FeatherIcon extends HTMLElement {
    connectedCallback() {
        this.innerHTML = feather.icons[this.getAttribute("name")].toSvg();
    }
}

customElements.define("feather-icon", FeatherIcon)

// I think only a module can import a module???
//import { Slim } from "slim-js";

class NotificationWidget extends Slim {
    constructor(eventIdentifer) {
        super();
        this.eventIdentifer = eventIdentifer;
    }
}

Slim.element(
    "notification-widget",
    `<p>
        <feather-icon name="arrow-right-circle"></feather-icon>
        {{this.eventIdentifer}}
    </p>`,
    NotificationWidget
)

class CounterWidget extends Slim {
    constructor(name) {
        super();
        this.name = name;
        this.count = 0;
    }
    increment() {
        this.count += 1;
    }
}

Slim.element(
    "counter-widget",
    `<p><b>{{this.name}}:</b> {{this.count}}</p>`,
    CounterWidget,
)

function startFollowingEvents() {
    console.log("Connecting to '/events'");
    const eventSource = new EventSource("/events");
    eventSource.addEventListener("newnumber", (event) => {
        let message = "Hello from Server " + event.data;
        handleEvent(message);
    })
    eventSource.addEventListener("direction", (event) => {
        window.directionCounter.increment();
        let message = "Heading " + event.data + "...";
        handleEvent(message);
    })
    eventSource.onerror = (err) => {
        console.log("Event Source Error Here " + err);
        startFollowingEvents();
    }
}

function handleEvent(message) {
    let node = new NotificationWidget(message);
    document.body.appendChild(node);
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("I have loaded!");
    window.directionCounter = new CounterWidget("Direction");
    document.body.appendChild(window.directionCounter);
    startFollowingEvents();
});
