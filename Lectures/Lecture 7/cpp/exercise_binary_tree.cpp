#include <string>
#include <iostream>

using namespace std;

/** Node beskriver ett binärt träd (rekursivt)
 * 
*/
class Node {
public:
    string name;
    Node * left;
    Node * right;

    Node(string name) {
        this->name = name;
        this->left = nullptr;
        this->right = nullptr;
    }

    int size() {
        int s = 1;

        if (this->left != nullptr) {
            s += this->left->size();
        }
        if (this->right != nullptr) {
            s += this->right->size();
        }

        return s;
    }

    int height(int height = 1) {
        // Vilken höjd får vi från vara barn?
        // Om vi inte har vänster eller höger barn, så blir nuvarande höjd max höjden
        int left_height = height;
        int right_height = height;

        if (this->left != nullptr) {
            left_height = this->left->height(height + 1);
        }
        if (this->right != nullptr) {
            right_height = this->right->height(height + 1);
        }

        return (left_height > right_height ? left_height : right_height);
    }

    int level(Node* root, int distance = 0) {
        // Vi vill gå rekursivt tills vi hittar vår nod, och räkna antal nivåer mellan

        if (this == root) {
            return distance;
        }

        if (root->left == nullptr && root->right == nullptr) {
            // Vi har kommit till botten av trädet, men ändå inte hittat vår nod!
            // Returnera -1 för att indikera att vi inte hittat den
            return -1;
        }

        int find_distance = -1;

        if (root->left != nullptr) {
            find_distance = level(root->left, distance+1);
            if (find_distance != -1) {
                return find_distance;
            }
        }
        if (root->right != nullptr) {
            find_distance = level(root->right, distance+1);
            if (find_distance != -1) {
                return find_distance;
            }
        }

        // Vi hittade den inte!
        return -1;
    }
};

int main() {
    Node root_node = Node("uggla");
    Node n1 = Node("hamster");
    Node n2 = Node("apa");
    Node n3 = Node("gorilla");
    Node n4 = Node("häst");
    Node n5 = Node("lemur");
    Node n6 = Node("pingvin");
    Node n7 = Node("varg");

    root_node.left = &n1;
    root_node.right = &n6;
    n1.left = &n2;
    n1.right = &n4;
    n2.right = &n3;
    // n3 has no children
    n4.right = &n5;
    // n5 has no chilcren
    n6.right = &n7;
    // n7 has no children
    
    cout << "root size:" << root_node.size() << endl;
    cout << "n6 size:" << n6.size() << endl;
    cout << "n7 size:" << n7.size() << endl;

    cout << endl;
    cout << "root height:" << root_node.height() << endl;
    
    cout << endl;
    cout << "n7 level:" << n7.level(&root_node) << endl;
    cout << "n3 level against n5:" << n3.level(&n5) << endl;
}