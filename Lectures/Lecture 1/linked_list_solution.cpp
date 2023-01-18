#include <iostream>
#include <assert.h>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

    // Default constructor
    Node()
    {
        data = 0;
        next = NULL;
    }

    // Constructor with data
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }

};

class LinkedList
{
public:
    Node *head;
    Node *tail;

    LinkedList()
    {
        head = NULL;
        tail = NULL;
    }

    void printList();
    int count();
    int sum();
    void append(int data);

};



void LinkedList::printList()
{
    Node *temp = head;

    // Check for empty list.
    if (head == NULL)
    {
        cout << "List empty" << endl;
        return;
    }
    // Traverse the list.
    while (temp != NULL)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "None" << endl;
}

int LinkedList::count() {
    Node * node = this->head;
    int count = 0;

    while (node != NULL) {
        // Ytterligare en nod, räkna upp
        count++;
        // Gå till nästa
        node = node->next;
    }

    return count;
}

int LinkedList::sum() {
    Node * node = this->head;
    int sum = 0;

    while (node != NULL) {
        sum += node->data;
        node = node->next;
    }

    return sum;
}

void LinkedList::append(int data) {
    Node * new_node = new Node(data);

    if (this->head == NULL) {
        // List is empty, set head and tail
        this->head = new_node;
        this->tail = new_node;
    } else {
        // List was not empty, add new node
        this->tail->next = new_node;
        this->tail = new_node;
    }
}

int main()
{
    LinkedList llist;
    llist.printList();

    //Node box1(1);
    //llist.head = &box1;
    llist.append(1);
    llist.printList();

    //Node box2(2);
    //box1.next = &box2;
    llist.append(2);
    llist.printList();

    //Node box3(3);
    //box2.next = &box3;
    llist.append(3);
    llist.printList();

    Node *currentNode = llist.head;
    // Börja på första noden och gå till next, tills vi kommer till slutet
    while (currentNode != NULL) {
        cout << currentNode->data << endl;

        // Gå vidare till nästa nod
        currentNode = currentNode->next;
    }

    cout << "LList length: " << llist.count() << endl;
    assert(llist.count() == 3);

    cout << "LList sum: " << llist.sum() << endl;
    assert(llist.sum() == 6);

    cout << "Append(4)" << endl;
    llist.append(4);
    cout << "LList length: " << llist.count() << endl;
    cout << "LList sum: " << llist.sum() << endl;
    llist.printList();
}