"""
1-Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso
2-Crea un nuevo archivo .py
3-Define una variable de cada tipo de primitivo
4-Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
5-Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
6-Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
7-Imprimir los resultados de las tareas anteriores
8-Envía el link del archivo en el repositorio con las respuesta
"""

#Punto 1: https://github.com/Ru-nai/Codelab_Variables_Python

#Punto 2: ---

#Punto 3:
var_Str = "Tomate" #Variable Cadena de Caracteres
var_Int = 82 #Variable Número Entero
var_Float = 4.1 #Variable Número Real/Float
var_Bool = False #Variable Booleana

#Punto 4:
vars_concatenadas = str(var_Str+" {}" + " {}" + " {}").format(var_Int, var_Float, var_Bool)

#Punto 5:
""" 
* El límite de Int en Python: dependiendo de la versión de Python, hay o no hay límite en los enteros. Por ejemplo, antes de Python 3,
si un número era demasiado grande o demasiado chico como para que "Int" lo contuviera, este número/variable se cambiaba automáticamente a
"Long," pues este tipo de dato contenía un valor sin importar qué tanta memoria/espacio de almacenamiento contuviera y si esto perjudicaba
el performance. Sin embargo, en Python 3, estos dos tipos de datos se unificaron y solo hay un tipo ahora (Int), y ahora un "Int" puede
almacenar valores tan grandes como haya memoria disponible. En Python 2 se podía obtener el valor máximo de Int con la constante "sys.maxint,"
mientras que en Python 3 esa función se eliminó pues ya no hay un límite para Int.
"""
"""
* El límite de Float en Python: a diferencia de los Int, los "Float" tienen valores mínimos y máximos que pueden representar, la mínima 
precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308. Aún así, los datos Float también tienen un valor especial llamado
"inf" que sirve para representar infinidad. Se puede obtener el valor máximo que un Float puede representar con la función: "sys.float_info.max,"
y se puede obtener el valor positivo mínimo que representa con: "sys.float_info.min;" y el valor mínimo negativo se puede obtener con:
"sys.float_info.max"
"""

#Punto 6 (la verdad no sé si entendí):
suma_pares_Int = 0
for i in range (var_Int + 1):
    if i % 2 == 0:
        #print(i)
        suma_pares_Int = suma_pares_Int + i

#Punto 7:

print (
       '\n' "* La variable con valor String es: " + var_Str,'\n',
       str("* La variable con valor Int es: "+" {}").format(var_Int),'\n',
       str("* La variable con valor Float es: "+" {}").format(var_Float),'\n',
       str("* La variable con valor Bool es: "+" {}").format(var_Bool),'\n',
       str("* Las variables concatenadas a la variable Str resulta en: "+" {}").format(vars_concatenadas),'\n',
       str("* La suma de los pares de la variable Int es: "+" {}").format(suma_pares_Int),'\n',
)





