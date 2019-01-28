# Minesweeper
Este es el clasico juego de buscaminas desarrollado en Python.
Para comenzar solo necesitamos:
- Tamaño del tablero.
- Cantidad de minas.
- Primer movimiento para comenzar a jugar.

Ejemplo: En este caso estableceremos el board size = 5, lo que significa que nos devolvera un tablero de 5x5; la cantidad de minas sera 2
que estaran distribuidas aleatoriamente.
Para llenar el valor de movimiento debemos insertar dos numeros (fila y columna) separados por una ","; como se muestra en la captura 
(0,0).

![capture1](https://user-images.githubusercontent.com/3207930/51855999-91849900-22fc-11e9-8ef9-eaa9215f5164.PNG)

Despues de a ver llenado estos primeros datos, presionaremos enter y mostrara el tablero del juego junto con el primer movimiento que 
escojimos. Hay algunas pistas que nos ayudaran a ganar el juego y son:
- Si en algun movimiento nos topamos con un valor 0 todos los 0 que esten conectados a este se mostraran

![capture2](https://user-images.githubusercontent.com/3207930/51856185-11aafe80-22fd-11e9-9d93-5632c21afbb8.PNG)

- Si en el siguiente movimiento nos topamos con un espacio cerca a una o mas minas, en ese espacio nos indicara la cantidad de bombas que se encuentran cerca.

![capture3](https://user-images.githubusercontent.com/3207930/51856381-939b2780-22fd-11e9-945b-fe728f0008b7.PNG)

Y asi jugaremos hasta que descubramos todos los espacios sin toparnos con alguna mina y ganaremos.

![capture4](https://user-images.githubusercontent.com/3207930/51856414-a4e43400-22fd-11e9-8b24-00978fcdfa16.PNG)


Si en alguno de esos movimientos caemos en el espacio de alguna bomba perderemos y se mostrará todo el tablero junto con las minas ([*])

![capture5](https://user-images.githubusercontent.com/3207930/51857054-4324c980-22ff-11e9-9b0f-4333e24e732a.PNG)


Entonces comenzemos a jugar!!! :D








