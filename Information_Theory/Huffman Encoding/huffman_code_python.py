""" 
This code is a simple implementation of huffman encoding
"""
from collections import Counter
from heapq import heappush, heappop

def huffman_encode(text):
    frequency = Counter(text)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heap = [[weight, [char, "0"]] for char, weight in frequency.items()]
    heap = [[weight, [char, "1"]] for char, weight in frequency.items()]
    heappush(heap, [weight1 + weight2, [char1 + char2, code1 + code2]])
    return dict(heappop(heap))

text = "ADBADEDBBDD"
encoded_text = "".join(huffman_encode(text)[c] for c in text)
print("Encoded text:", encoded_text)
