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
        next = nullptr;
    }

    // Constructor with data
    Node(int data)
    {
        this->data = data;
        this->next = nullptr;
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
        head = nullptr;
    }

    void push(int data);
    bool pop(int &data);
    bool peek(int &data);
    bool isEmpty();
    bool swap(int i, int j);
    friend std::ostream& operator<< (std::ostream &os, const Storage* storage);
};
#endif
