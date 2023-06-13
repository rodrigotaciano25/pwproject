// Função para adicionar números ao visor da calculadora
function adicionarNumero(numero) {
    var visor = document.getElementById("visor");
    visor.value += numero;
}

// Função para realizar o cálculo
function calcular() {
    var visor = document.getElementById("visor");
    var resultado = eval(visor.value);
    visor.value = resultado;
}

// Função para limpar o visor
function limparVisor() {
    var visor = document.getElementById("visor");
    visor.value = "";
}

// Função para o dark/light mode

const darkModeButton = document.getElementById("darkModeButton");
const h1 = document.querySelector("h1");
const body = document.body;

darkModeButton.addEventListener("click", function() {
  body.classList.toggle("dark-mode");
  h1.classList.toggle("dark-mode");
  if (body.classList.contains("dark-mode")) {
    darkModeButton.textContent = "Desativar Light Mode";
  } else {
    darkModeButton.textContent = "Ativar Light Mode";
  }
});


// Função da data atual

function getDataAtual() {
  var data = new Date();
  var dia = data.getDate();
  var mes = data.getMonth() + 1;
  var ano = data.getFullYear();
  var dataAtual = dia + '/' + mes + '/' + ano;
  return dataAtual;
}

document.getElementById('data-atual').innerHTML = getDataAtual();