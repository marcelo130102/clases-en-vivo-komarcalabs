# Decoradores

def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Podemos agregar código antes")
        resultado = funcion(*args, **kwargs)
        print("Podemos agregar código después")
        return resultado
    return nueva_funcion


@decorador
def funcion_a_decorar():
    print("Esta es una función a decorar")

funcion_a_decorar()