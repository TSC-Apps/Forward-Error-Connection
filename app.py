from generator import generate_bits
from decoder import decode
from coder import triple_code
from canal import bsc

quantity = int(input('Podaj ilosc bitow informacji do wygenerowania: '))

# generacja
lst = generate_bits(quantity)
print(f"Przykładowy ciąg:\t\t\t\t {lst}")

# kodowanie
coded_lst = triple_code(lst)
print(f"Zakodowany ciąg:\t\t\t\t {coded_lst}")

# przepusczenie przez kanał
output, wrongBits = bsc(coded_lst, 0.2)
print(f"Ciąg po przejsciu przez kanał:\t {output}")

# dekodowanie
decoded_lst = decode(output)
print(f"Odkodowany ciąg:\t\t\t\t {decoded_lst}")
print(f"BER: {wrongBits / len(coded_lst)}") #BER ma sie odnosic do zakodowanej czy nie zakodowanej liczby?
