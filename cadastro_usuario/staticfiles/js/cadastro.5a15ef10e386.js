var senha = document.getElementById('senha')
var confirma_senha = document.getElementById('confirma_senha')
senha.onkeyup = validaSenha
confirma_senha.onkeyup = validaSenha

var nome = document.getElementById('nome')
nome.onchange = verificaVazio

var email = document.getElementById('email')
email.onchange = verificaVazio

var pais = document.getElementById('pais')
pais.onchange = verificaVazio

var estado = document.getElementById('estado')
estado.onchange = verificaVazio

var municipio = document.getElementById('municipio')
municipio.onchange = verificaVazio

var rua = document.getElementById('rua')
rua.onchange = verificaVazio

var forms = document.querySelectorAll('.needs-validation')
Array.prototype.slice.call(forms)
.forEach(function (form) {
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
        }
        else{
            removeMasks()
        }
        form.classList.add('was-validated')
    }, false)
})

function removeMasks(){
    var elements = [document.getElementById('cpf'), document.getElementById('pis'), document.getElementById('cep')]
    for(var element of elements){
        element.value = element.value.replace(/[^0-9]/g,'')
    }
   
}

function cpfMask(element){
    if(element.value.match(/^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$/)){
        element.setCustomValidity('')
    }
    else{
        element.setCustomValidity('Formato do cpf incorreto')
    }
    if(element.value.length == 3 || element.value.length == 7){
        element.value += '.'
    }
    if(element.value.length == 11){
        element.value += '-'
    }
}

function pisMask(element){
    if(element.value.match(/^[0-9]{3}\.[0-9]{3}\.[0-9]{4}-[0-9]{1}$/)){
        element.setCustomValidity('')
    }
    else{
        element.setCustomValidity('Formato do pis incorreto')
    }
    if(element.value.length == 3 || element.value.length == 7){
        element.value += '.'
    }
    if(element.value.length == 12){
        element.value += '-'
    }
}

function cepMask(element){
    if(element.value.match(/^[0-9]{5}-[0-9]{3}$/)){
        element.setCustomValidity('')
    }
    else{
        element.setCustomValidity('Formato do pis incorreto')
    }
    if(element.value.length == 5){
        element.value += '-'
    }
}

function validaSenha(){
    if(senha.value != confirma_senha.value){
        senha.setCustomValidity('Senhas diferentes')
        confirma_senha.setCustomValidity('Senhas diferentes')
    }
    else{
        senha.setCustomValidity('')
        confirma_senha.setCustomValidity('')
    }
}

function verificaVazio(event){
    event.target.value = event.target.value.trim()
    if(event.target.value == 0){
        event.target.setCustomValidity('Campo somente com espaços')
    }
    else{
        event.target.setCustomValidity('')
    }
}