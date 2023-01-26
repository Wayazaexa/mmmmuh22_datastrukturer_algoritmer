#include <iostream>

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
private:
    int lsize; // Håller koll på storleken för snabbare åtkomst. Måste ändras när noder tas bort eller läggs till
public:
    Node *head;
    Node *tail;

    LinkedList()
    {
        head = NULL;
        tail = NULL;
    }

    friend ostream & operator << (ostream &out, const LinkedList &list);    
    void printList();
    int size() {
        return this->lsize;
    }
    int count() { 
        return size();
    }
    bool contains(int data);                //finns 
    int sum();
    void append(int data);
    void prepend(int data);
    void insert(int data, int after_data);  //Lägger till nod med data, efter en nod innehållande "after_data"
    void remove_first_node();
    void remove_last_node();
    void remove_node(int data);             //Tar bort nod som innehåller "data"
};

ostream & operator << (ostream &out, const LinkedList &list) 
{
    out << "[";

    string separator;
    Node * n = list.head;
    // Iterate all nodes in list and print
    while (n!=NULL) {
        out << separator << "'" << n->data << "'";
        separator = ", ";
        n = n->next;
    }
    out << "]";
    return out;
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

/**
 * Return the sum of all data in the list
*/
int LinkedList::sum() {
    Node * node = this->head;
    int sum = 0;

    while (node != NULL) {
        sum += node->data;
        node = node->next;
    }

    return sum;
}

/** 
 * Add the data to a node at the end of the list
*/
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

    this->lsize++;
}

/**
 * Add the data to a node at the start of the list
*/
void LinkedList::prepend(int data) {
    // 1. Skapa ny nod
    Node * new_node = new Node(data);

    // 2. Sätt den nya nodes "next" till listans head
    new_node->next = this->head;

    // 3. Flytta listans head till den nya noden
    this->head = new_node;

    // 4. Om listan är tom: Uppdatera tail
    if (this->tail == NULL) {
        this->tail = new_node;
    }

    this->lsize++;
}

/**
 * Insert data in a new node, placed after the (first) node containing 'after_data'
*/
void LinkedList::insert(int data, int after_data) {
    // 1. Skapa ny nod
    Node * new_node = new Node(data);

    // Är listan tom?
    if (this->head == NULL) {
        throw std::out_of_range("Can't insert into an empty list");
    }

    // 2. Hitta rätt ställe i listan
    Node * current = this->head;
    while (current->data != after_data) {
        current = current->next;
        if (current == NULL) {
            // Om vi inte hittar datan kastar vi exception.
            // Todo: Det här bör kanske hanteras på ett bättre sätt, eller i alla fall definera en egen exception.
            throw std::out_of_range("Data not found in list");
        }
    }

    // 3. Sätt den nya nodens "next" till nästa nod
    new_node->next = current->next;

    // 4. Sätt nuvarande nodens "next" till nästa nod
    current->next = new_node;

    this->lsize++;
}

/**
 * Remove the first node from the list
*/
void LinkedList::remove_first_node() {
    // Om listan är tom, ge exception
    if (this->head == NULL) {
        throw std::out_of_range("list is empty");
    }

    // Flytta listans head till nästa nod
    this->head = this->head->next;

    // Om vi tog bort sista elementet så ska vi uppdatera tail också
    if (this->head == NULL) {
        this->tail = NULL;
    }

    this->lsize--;
}

/** 
 * Remove the last node from the list
*/
void LinkedList::remove_last_node() {
    // Vi har inte dubbellänkad lista, så vi måste stega igenom till (näst sista)

    // 1. Om listan är tom, ge exception
    if (this->head == NULL) {
        throw std::out_of_range("list is empty");
    }

    // 2. Skapa två tillfälliga pekare "current" och "previous"
    Node * current = this->head;
    Node * previous = this->head;

    // 3. Stega till "current" är sista noden (prevous blir den vi ska ha kvar)
    while (current != NULL) {
        if (current->next == NULL) {
            if (current == this->head) {
                // 4a. Specialfall, sista och första noden vara samma. Dvs listan hade bara en nod --> töm listan
                this->head = NULL;
                this->tail = NULL;
            } else {
                // 4b. Sätt previous->next till NULL (sista noden)
                previous->next = NULL;
                this->tail = previous;
            }
        }

        previous = current;
        current = current->next;
    }

    this->lsize--;
}

/**
 * Remove the (first) node containing 'data' 
*/
void LinkedList::remove_node(int data) {

    // 1. Om listan är tom, ge exception
    if (this->head == NULL) {
        throw std::out_of_range("list is empty");
    }

    // 2. Börja med att stega från listans start
    Node * current = this->head;
    Node * previous = this->head;

    while (current != NULL) {
        // Har vi hittat vår nod?
        if (current->data == data) {
            // Specialfall: Första noden
            if (current == this->head) {
                // 3a. Flytta head ett steg åt höger
                this->head = current->next;
            } else {
                // 3b. Vi är inte i starten av listan. Flytta förra elementets next ett steg åt höger
                previous->next = current->next;
            }

            // 4. Tog vi bort första eller sista noden?
            if (this->head == NULL) {
                // ... första
                this->tail == NULL;
            }
            else if (current == this->tail) {
                // Sista... Flytta tail ett steg åt vänster
                this->tail = previous;
            }

            // Endast första matchande noden tas bort. Avsluta metoden.
            this->lsize--;
            return;
        }

        // Vi har inte hittat det vi sökte: Flytta båda pekarna
        previous = current;
        current = current->next;
    }
}
