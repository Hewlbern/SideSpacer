

function RemoteWorkers() {
    var x = document.getElementById("paragraph1");
    var y = document.getElementById("paragraph2");
    var z = document.getElementById("paragraph3");
    if (x.style.display === "block") {
        x.style.display = "block";
        y.style.display = "none";
        z.style.display = "none";

    } else {
        x.style.display = "block";
        y.style.display = "none";
        z.style.display = "none";
    }
}


function Startups() {
    var x = document.getElementById("paragraph1");
    var y = document.getElementById("paragraph2");
    var z = document.getElementById("paragraph3");
    if (y.style.display === "none") {
        y.style.display = "block";
        x.style.display = "none";
        z.style.display = "none";
    } else {
        y.style.display = "block";
        x.style.display = "none";
        z.style.display = "none";
    }
}


function OfficeGoers() {
    var x = document.getElementById("paragraph1");
    var y = document.getElementById("paragraph2");
    var z = document.getElementById("paragraph3");
    if (z.style.display === "none") {
        z.style.display = "block";
        y.style.display = "none";
        x.style.display = "none";
    } else {
        z.style.display = "block";
        x.style.display = "none";
        y.style.display = "none";
    }
}

