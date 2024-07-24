

const area= document.getElementById("area");
const text2= document.getElementById("text2");

function ocultarText() {
    text2.style.display = "none";
}

function mostrarText() {
    text2.style.display = "block";
}

area.onmouseout = ocultarText;
area.onmouseover = mostrarText;


