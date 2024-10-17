# Segundo-Parcial

Para los tres puntos debemos tener instalado el antlr4

Tras esto, debemos crear un entorno virtual que se hace de la siguiente forma

    python3 -m venv env

Ya creado el entorno virtual lo activaremos de la siguiente forma:

    source env/bin/activate

Instalaremos el Python con el antlr4 en el entorno

    pip install antlr4-python3-runtime

Crearemos los archivos que se generan automaticamente por el antlr4 de la siguiente manera:

1. Numeros complejos:

Crearemos los archivos que se generan automaticamente por el antlr4 de la siguiente manera:

       antlr4 -Dlanguage=Python3 Expr.g4
       antlr4 -visitor -Dlanguage=Python3 Expr.g4
   
Tras crear los archivos lo ejecutamos con el siguiente comando

       python main.py entrada.txt


2. Funciones MAP y FILTER

Crearemos los archivos que se generan automaticamente por el antlr4 de la siguiente manera:

       antlr4 -Dlanguage=Python3 MapFunction.g4
       antlr4 -visitor -Dlanguage=Python3 MapFunction.g4
   
Tras crear los archivos lo ejecutamos con el siguiente comando

       python3 main.py entrada.txt

3. Trasformada de Fourier

Para este punto debemos tener intalados las bibliotecas de numpy y mathplotlib, si no estan instaladas se instalan de la siguiente manera:

    pip install numpy
    pip install matplotlib

Crearemos los archivos que se generan automaticamente por el antlr4 de la siguiente manera:

       antlr4 -Dlanguage=Python3 Grammar.g4
       antlr4 -visitor -Dlanguage=Python3 Grammar.g4

Tras crear los archivos lo ejecutamos con el siguiente comando

      python3 myVisitor.py


    

   

     








    

