document.querySelector('#btnMain').addEventListener('click', main)
document.querySelector('#btnLogin').addEventListener('click', logearse)
document.querySelector('#btnRegister').addEventListener('click', registrar)
document.querySelector('#btnBillboard').addEventListener('click', cartelera)
document.querySelector('#btnContact').addEventListener('click', contactar)

function main(){
    window.location.href=window.location.origin+"/home"
}
function logearse(){
    window.location.href=window.location.origin+`/login`
}
function registrar(){
    window.location.href=window.location.origin+`/register`
}
function cartelera(){
    window.location.href=window.location.origin+`/billboard`
}
function contactar(){
    window.location.href=window.location.origin+"/contact"
}