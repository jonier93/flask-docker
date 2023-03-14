document.querySelector('#btnCuenta').addEventListener('click', actualizarDatos)

function actualizarDatos(){
    //window.location.href=`prueba/${100}`
    fetch('/datos', { // Debido al comportamiento asincrónico de fetch, es necesario utilizar promesas para poder redirigir a otra URL, desde el backend no cargaría sin solicitar desde el frontend después de las promesas
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(correo),
    })
    .then(response => response.json())
    .then(data =>  window.location.href=`actualizar/${data.name}/${data.lastname}/${data.identification}/${data.email}/""`) 
}