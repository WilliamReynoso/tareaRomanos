El programa detecta numeros romanos en las letras de una lista de palabras que fueron proveidas, a estas palabras se les imprime junto con su valor numerico del primer numero romano **valido** que se ha detectado.
Se respetaron las siguientes reglas y excepciones para cumplir con los numeros romanos:

# Tres reglas…

> Suma
> Cuando un símbolo está situado después (a la derecha) de otro valor más grande, se suman. Por ejemplo: XI = 10 + 1 = 11.

> Resta
> Cuando un símbolo está situado antes (a la izquierda) de otro valor más grande, se restan. Por ejemplo: XL = 50 − 10 = 40. De este modo, cuando un símbolo está entre dos números de valor más grande, se resta del símbolo de la derecha. Por ejemplo: XIX = 10 + (10 − 1) = 19.
> Números grandes

# ¡Y tres excepciones!

> No repetir un símbolo más de 3 veces seguidas
> No puede haber más de 3 símbolos iguales seguidos. Por ejemplo, el 4 no se puede escribir IIII (sino IV).

> No repetir los símbolos que empiezan por 5
> Los símbolos V, L y D (5, 50 y 500, respectivamente) no se pueden repetir.
> No todos los símbolos pueden restar

> Solo los símbolos I, X y C (1, 10 y 100, respectivamente) pueden restar, y solo pueden restar a los 2 símbolos inmediatamente superiores. Por tanto, I solo puede restar a V o X, X solo puede restar a L o C, y C solo puede restar a M. Es decir, que solo hay 6 combinaciones de resta posibles: IV = 5 − 1 = 4; IX = 10 − 1 = 9; XL = 50 − 10 = 40; XC = 100 − 10 = 90; CD = 500 − 100 = 400; y CM = 1000 − 100 = 900.
