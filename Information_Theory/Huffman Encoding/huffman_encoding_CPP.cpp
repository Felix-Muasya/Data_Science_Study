#include <iostream>
#include <unordered_map>
#include <queue>
#include <vector>
#include <string>

using namespace std;

struct Node {
    char character;
    int frequency;
    Node *left, *right;

    Node(char character, int frequency) {
        this->character = character;
        this->frequency = frequency;
        this->left = this->right = nullptr;
    }
};

struct Compare {
    bool operator()(Node *a, Node *b) {
        return a->frequency > b->frequency;
    }
};

unordered_map<char, string> huffman_code;

void build_huffman_tree(string text) {
    unordered_map<char, int> frequency;
    for (char c : text) {
        frequency[c]++;
    }

    priority_queue<Node*, vector<Node*>, Compare> heap;
    for (auto p : frequency) {
        heap.push(new Node(p.first, p.second));
    }

    while (heap.size() != 1) {
        Node *left = heap.top();
        heap.pop();
        Node *right = heap.top();
        heap.pop();
        int sum = left->frequency + right->frequency;
        heap.push(new Node('\0', sum, left, right));
    }

    void encode(Node *root, string str) {
        if (!root) {
            return;
        }

        if (root->character != '\0') {
            huffman_code[root->character] = str;
        }

        encode(root->left, str + "0");
        encode(root->right, str + "1");
    }

    Node *root = heap.top();
    encode(root, "");
}

string huffman_encode(string text) {
    build_huffman_tree(text);
    string encoded = "";
    for (char c : text) {
        encoded += huffman_code[c];
    }
    return encoded;
}

int main() {
    string text = "ADBADEDBBDD";
    string encoded = huffman_encode(text);
    cout << "Encoded text: " << encoded << endl;
    return 0;
}
