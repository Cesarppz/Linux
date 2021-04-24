str(mtcars)

class(mtcars$vs)

#Cambio los tipo de variables
mtcars$vs = as.logical(mtcars$vs)
mtcars$am = as.logical(mtcars$am)
