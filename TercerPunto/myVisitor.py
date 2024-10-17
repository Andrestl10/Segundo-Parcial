import numpy as np
import matplotlib.pyplot as plt
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser

class ListVisitor(ParseTreeVisitor):
    def visitList(self, ctx:GrammarParser.ListContext):
        elements = [self.visit(element) for element in ctx.element()]
        return np.array(elements)

    def visitElement(self, ctx:GrammarParser.ElementContext):
        return float(ctx.NUMBER().getText())

def main():
    input_stream = InputStream("[ 0.        ,  3.25276264,  5.38102044,  5.68906404,  4.17499424,1.53073373, -1.12296426, -2.66528832, -2.40414157, -0.34113407,2.82842712,  5.98055012,  7.99135056,  8.16584324,  6.50295236,3.69551813,  0.8652998 , -0.8658029 , -0.80452922,  1.04874307,4.        ,  6.9265956 ,  8.70603594,  8.64476226,  6.74315233,3.69551813,  0.62509984, -1.34472192, -1.5192146 ,  0.1026976 ]")  # Aquí pon la lista que desees analizar
    lexer = GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GrammarParser(token_stream)
    tree = parser.list()
    
    visitor = ListVisitor()
    array = visitor.visit(tree)
    
    time = np.arange(0, 3, 0.1)
    
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(time, array)
    plt.title('Original Time series')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    fourier_transform = np.fft.fft(array)
    frequencies = np.fft.fftfreq(len(array), 0.01)
    
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, np.abs(fourier_transform))
    plt.title('Fourier Transform')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')

    plt.show()

if __name__ == '__main__':
    main()

