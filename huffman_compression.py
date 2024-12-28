import heapq
from collections import defaultdict

# Huffman Tree Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(text):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Priority queue for building the tree
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Build the tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

# Generate Huffman Codes
def generate_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

# Encode text using Huffman Codes
def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)

    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root, codes

# Decode Huffman Encoded text
def huffman_decode(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

if __name__ == "__main__":
    print("Huffman Coding Data Compression")
    user_input = input("Enter text to compress: ")

    encoded_text, tree, codes = huffman_encode(user_input)
    print(f"Encoded Text: {encoded_text}")
    print(f"Huffman Codes: {codes}")

    decoded_text = huffman_decode(encoded_text, tree)
    print(f"Decoded Text: {decoded_text}")

    if user_input == decoded_text:
        print("Success! Compression and Decompression work correctly.")
    else:
        print("Error! There is a mismatch between original and decompressed text.")
