teste <- "valor3"


switch(teste,
       "valor1" = {print(teste)},
         "valor2" = {print(teste)},
           "valor3" = {print(teste)},
             "default" = {print(teste)})


x = 1
y = -1
if (x > 0) {
  if (y > 0) {
    quadrante = "Quadrante 1"
    cat( paste0("O ponto (", x, ", ", y, ") pertence ao ", quadrante))
  } else {
    quadrante = "Quadrante 4"
    cat( paste0("O ponto (", x, ", ", y, ") pertence ao ", quadrante))
  }
} else {
  if (y > 0) {
    quadrante = "Quadrante 2"
    cat( paste0("O ponto (", x, ", ", y, ") pertence ao ", quadrante))
  } else {
    quadrante = "Quadrante 3"
    cat( paste0("O ponto (", x, ", ", y, ") pertence ao ", quadrante))
  }
}

numero <- 4913742371422
ifelse(numero %% 2 == 0, "par", 
       "impar")