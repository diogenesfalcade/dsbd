classificaComb <- function(meioDeTransp){
  combustivel <- switch (meioDeTransp,
          "Carro" = c("Gasolina", "Diesel", "Eletrecidade", "Gás Natural"),
          "Moto" = "Gasolina",
          "Bicicleta"= "Humana (sem cobutível)",
          "Ônibus"= c("Dieel", "Gás Natural"),
          "Trem"= c("Eletricidade", "Diesel"),
          "Avião"= "Queroee",
          "Barco"= c("Diesel", "Gasolina")
  )
  return(combustivel)
}

veiculo <- "Carro"
classificaComb(veiculo)


converteTemp <- function(temp, unidade){
  if(unidade == 'Celsius') {
    fahrenheit <- temp * 9/5 +32
    return(fahrenheit)
  } else if(unidade == 'Fahrenheit'){
    celsius <- (temp - 32) * 5/9
    return(celsius)
  } else
    stop('Unidade invalida')
}

converteTemp(0, 'Celsius')

calcula_imc <- function(peso, altura) {
  imc <- peso / altura^2
  if(imc < 18.5) {
    mensagem <- "Abaixo do Peso"
  } else if(imc >= 18.5 & imc < 25) {
    mensagem <- "Peso Normal"
  } else if(imc >= 25 & imc < 30) {
    mensagem <- "Sobrepeso"
  } else {
    mensagem <- "Obesidade"
  }
  return( list(imc = imc, mensagem = mensagem))
}
calcula_imc(70, 1.75)