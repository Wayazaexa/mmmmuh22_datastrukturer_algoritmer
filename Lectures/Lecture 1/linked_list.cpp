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

    LinkedList()
    {
        head = NULL;
    }

    int count();
    int sum();
    void append(int data);
    void printList();

};

int LinkedList::count()
{
    Node *temp = head;
    int sum = 0;

    while (temp != NULL)
    {
        sum += 1;
        temp = temp->next;
    }
    return sum;
}

int LinkedList::sum()
{
    Node *temp = head;
    int sum = 0;

    while (temp != NULL)
    {
        sum += temp->data;
        temp = temp->next;
    }
    return sum;
}

void LinkedList::append(int data)
{
    Node *new_node = new Node(data);

    if (head == NULL)
    {
        head = new_node;
    }
    else{
        Node *temp = head;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = new_node;
    }
}

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

    int size = llist.count();
    assert(size == 3);
    cout << "The list contains " << size << " nodes.\n";

    int sum = llist.sum();
    assert(sum == 6);
    cout << "The sum of the data in the list is " << sum << ".\n";

    Node *currentNode = llist.head;
    // Börja på första noden och gå till next, tills vi kommer till slutet
    while (currentNode != NULL) {
        cout << currentNode->data << endl;

        // Gå vidare till nästa nod
        currentNode = currentNode->next;
    }
}