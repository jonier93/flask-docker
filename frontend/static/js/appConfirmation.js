if (opcion == 0) {
    confirm("Error: el correo ya se encuentra registrado")
    window.location.href="register"
}
else if (opcion == 1) {
    confirm("Usuario creado exitosamente")
    window.location.href=`login`
}
else if (opcion == 2) {
    confirm("Datos de usuario actualizados")
    window.location.href=`login`
}
else if (opcion == 3 ) {
    confirm("Error: Contraseña incorrecta")
    window.location.href="login"
}
else if (opcion == 4) {
    confirm("Error: El usuario no existe")
    window.location.href="login"
}
else if (opcion == 5) {
    confirm("Error: La cedula ya se encuentra registrada")
    window.location.href="register"
}
//setTimeout (()=> {window.location.href=`home`}, 3000)