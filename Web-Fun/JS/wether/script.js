function cookies() {
    var i = document.querySelector(".cookie");
    i.remove();
}


function cityClk() {
    alert("Welcome in my page");
}


function selectDeg(deg) {
    var  theDeg = document.querySelectorAll(".converter");

    if (deg == 'F') {
        for (var i = 0; i < theDeg.length; i++) {
            theDeg[i].innerText = Math.round(((9 / 5) * theDeg[i].innerText)+ 32);
        }
    }
    else {
        for (var i = 0; i < theDeg.length; i++) {
            theDeg[i].innerText = Math.round(((5 / 9)*(theDeg[i].innerText - 32)));
        }

    }
}

