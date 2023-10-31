#COMPARADORES:


x <- 1  # Atribuição de X
x > 10  # Falso
x <= 2  # Verdadeiro
x == 3  # Falso
x != 'casa' # Verdadeiro
x > 0 & x < 4 # X está entre 0 e 4 -> Verdadeiro
!(x > 0 & x < 4) # X não está entre 0 e 4 -> Falso
x < 2 | x > 2 # X é menor que 2 OU maior que 2 

is.numeric(2)  # Verdadeiro
is.character('a')  # Verdadeiro
is.logical('casa')  # Falso
is.null(NULL)  # Verdadeiro
is.finite(log(0))  # Falso -> R = -infinito
is.na(x)  # Falso

x <- 10
if (x > 5) {
    cat('x é um número maior que 5\n')
}

x <- 5
is (x >5) {
    cat('x é um número maior que 5')
} else if (x >= 0 & x < 5) {
    cat('x está entre 0 e (inclusive) 5')
} else if (x == 5) {
    cat('X é exatamente igual a 5')
} else {
    cat('x é negativo')
}