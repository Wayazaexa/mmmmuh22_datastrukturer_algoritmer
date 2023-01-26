#ifndef storage_nju7654ewdfghjnbvcfr67890
#define storage_nju7654ewdfghjnbvcfr67890

#include <iostream>

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

class Storage
{
public:
    Node *head;

    /** Default constructor
     * 
    */
    Storage()
    {
        head = NULL;
    }

    void push(int data);
    bool pop(int &data);
    bool peek(int &data);
    bool isEmpty();
    bool swap(int i, int j);
};

#endif
