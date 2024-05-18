n <- 15
Fibonacci <- numeric(n)
Fibonacci[1] <- 1
Fibonacci[2] <- 1

for (i in 3:n) {
  Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]
}
Fibonacci


soma <- 0
n <- 0
repeat {
  dado1 <- sample(1:6, 1, replace = FALSE)
  dado2 <- sample(1:6, 1, replace = FALSE)
  soma <- dado1 + dado2
  n <- n + 1
  if (soma <= 5) {
    break
  }
}
n

