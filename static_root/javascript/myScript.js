

function Swap1() {
    var x = document.getElementById("HomeNav");
    var y = document.getElementById("SpacesNav");
    var z = document.getElementById("PricingNav");
    var a = document.getElementById("HowitworksNav");
    var b = document.getElementById("ContactNav");
    var c = document.getElementById("LogOutNav");
    var d = document.getElementById("SignUpNav");
    var e = document.getElementById("LogInNav");
    if (x.classList.contains ('active')) {
        y.classList.remove('active');
        z.classList.remove('active');
        a.classList.remove('active');
        b.classList.remove('active');
        c.classList.remove('active');
        d.classList.remove('active');
        e.classList.remove('active');

    } else {
        x.classList.contains ('active');
        y.classList.remove('active');
        z.classList.remove('active');
        a.classList.remove('active');
        b.classList.remove('active');
        c.classList.remove('active');
        d.classList.remove('active');
        e.classList.remove('active');
    }
}


if (y.classList.contains ('active')) {
    x.classList.remove('active');
    z.classList.remove('active');
    a.classList.remove('active');
    b.classList.remove('active');
    c.classList.remove('active');
    d.classList.remove('active');
    e.classList.remove('active');

} else {
    x.classList.contains ('active');
    y.classList.remove('active');
    z.classList.remove('active');
    a.classList.remove('active');
    b.classList.remove('active');
    c.classList.remove('active');
    d.classList.remove('active');
    e.classList.remove('active');
}




