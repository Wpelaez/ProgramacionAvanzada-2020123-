var formularioColor = document.forms["cajaTexto"]

formularioColor.addEventListener("submit", function(e){
    e.preventDefault()
    valorColor = formularioColor.querySelector("#color").value
    var caja = document.createElement("div");
    caja.setAttribute("class", "caja");
    var texto = document.createElement("h1")
    texto.textContent = "PRUEBA"
    texto.setAttribute("style", "background-color:" + valorColor + ";")
    caja.appendChild(texto)
    body = document.querySelector("body");
    body.appendChild(caja)
    formularioColor.reset()
});




