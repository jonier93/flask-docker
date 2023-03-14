document.querySelector('button').addEventListener('click', validation)

function validation(event){
    let aux = 0
    if(document.getElementById('Check').checked == false){
        event.preventDefault() // Evita que el formulario sea enviado antes de las validaciones correspondientes
        alert("Debe aceptar los terminos")
        aux=1;
    }
    else {
        if (document.getElementById("name_id").value == ""){
            event.preventDefault()
            alert("Debe ingresar un nombre")
            aux=1;
        }
        else if (document.getElementById("lastname_id").value == "") {
            event.preventDefault()
            alert("Debe ingresar un apellido")
            aux=1;
        }        
        else if (document.getElementById("email_id").value == "") {
            event.preventDefault()
            alert("Debe ingresar un email")
            aux=1;
        }
        else if (document.getElementById("password_id").value == "") {
            event.preventDefault()
            alert("Debe ingresar una contraseña")
            aux=1;
        }
    }
    if (aux == 0) {
        document.getElementById("identification_id").disabled=false
    }    
}

if (confirmation == 1){
    document.getElementById("name_id").value = nombre
    document.getElementById("lastname_id").value = lastname
    document.getElementById("identification_id").value = identification
    document.getElementById("email_id").value = email
    //document.getElementById("password_id").value = password

    document.getElementById("identification_id").disabled=true //Para deshabilitar la casilla y no se compueda cambiar el ID de la persona
}

