

# Huffman Coding Data Compression

This project demonstrates a basic implementation of Huffman Coding, a popular data compression algorithm. Huffman Coding is used to encode data efficiently by assigning shorter codes to frequently used characters and longer codes to less frequent ones. This results in reduced storage space and faster transmission times for the compressed data.

## Features
- **Text Compression**: Compress input text into a binary representation using Huffman Coding.
- **Text Decompression**: Decompress the binary representation back into the original text.
- **Character Frequency Analysis**: Analyze the frequency of each character in the input text and build a Huffman Tree.
- **Huffman Codes**: Generate unique binary codes for each character based on their frequency.

## How It Works
1. **Input Text**: The user provides a text input to compress.
2. **Frequency Calculation**: The frequency of each character is calculated.
3. **Huffman Tree Construction**: A binary tree is constructed where each node represents a character and its frequency.
4. **Code Assignment**: Binary codes are assigned to characters based on their position in the Huffman Tree.
5. **Compression**: The input text is encoded into a binary string using the Huffman codes.
6. **Decompression**: The binary string is decoded back into the original text using the Huffman Tree.

## Example
### Input:
```
I am an electrical and electronics engineer.
```
### Output:
**Encoded Text:**
```
1101001010001000010100001010111101111110010110110010010010000111101000010110110101111011111100101101100110101010100100110001110111101010001010010101111111100110111
```
**Huffman Codes:**
```
{'a': '000', 'c': '001', 'n': '010', 't': '0110', 'l': '0111', 'm': '10000', 'g': '100010', 's': '100011', 'i': '1001', ' ': '101', 'r': '1100', 'I': '110100', 'o': '110101', 'd': '110110', '.': '110111', 'e': '111'}
```
**Decoded Text:**
```
I am an electrical and electronics engineer.
```

## Requirements
- Python 3.7+
- Standard Python libraries: `heapq`, `collections`


## Acknowledgments
- Huffman Coding Algorithm: [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)



