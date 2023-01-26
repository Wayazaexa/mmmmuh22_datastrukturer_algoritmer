#include <iostream>
#include "storage.hh"

/** Create a Node to hold the data, then put it at the head of the list.
 * @param text The data for the new node
*/
void Storage::push(int data)
{
    Node* new_node = new Node(data);
    new_node->next = head;
    head = new_node;
}

/** Remove the head Node and return its data.
 * 
 * @param [out] The data (only valid if return true)
 * @return True if there is a node to return
*/
bool Storage::pop(int &data)
{
    if (head)
    {
        data = head->data;
        Node* tmp = head;
        head = head->next;
        delete tmp;
        return true;
    }
    else
        return false;
}

/**
 * Return the data from the head Node, without removing it.
 * 
 * @param [out] The data (only valid if return true)
 * @return True if text has been returned successfully (there is a node)
*/
bool Storage::peek(int &data)
{
    if (head)
    {
        data = head->data;
        return true;
    }
    else
        return false;
}

/**
 * Return True if the list is empty, otherwise False 
 * 
 * @return True if the storage is empty
*/
bool Storage::isEmpty()
{
    return !head;
}

/**
 * Swaps the nodes at position i and j.
 * 
 * @return Returns true if successful, otherwise false (e.g. outside range)
*/
bool Storage::swap(int i, int j)
{
    if (this->isEmpty())
        return false;
    if (i == j) // return true if i and j are the same
        return true;
    if (i < 0 || j < 0) // return false if i or j is out of bounds
        return false;
    
    Node* iPrev = head;
    Node* jPrev = head;
    Node* iCurr;
    Node* jCurr;
    Node* tmp;
    // To ensure I know which is the smaller index, I create new variables.
    int ii = std::min(i, j);
    int jj = std::max(i, j);
    
    if (ii == 0)
    {
        iCurr = head;
        jj--;

        // Set jPrev to the node before index jj
        while (jj > 0)
        {
            jPrev = jPrev->next;
            if (jPrev->next == NULL) // Return false if jj is out of bounds
                return false;
            jj--;
        }
        jCurr = jPrev->next;

        // Swap iCurr and jCurr
        tmp = jCurr->next;
        if (iCurr == jPrev) // Special case if iCurr and jCurr are adjacent
        {
            jCurr->next = iCurr;
        }
        else
        {
            jCurr->next = iCurr->next;
            jPrev->next = iCurr;
        }
        iCurr->next = tmp;
        head = jCurr;

        return true;
    }
    else
    {
        ii--;
        jj--;

        // Set iPrev to the node before index ii
        while (ii > 0)
        {
            iPrev = iPrev->next;
            if (iPrev->next == NULL) // Return false if ii is out of bounds
                return false;
            ii--;
            jPrev = jPrev->next;
            jj--;
        }
        iCurr = iPrev->next;

        // Set jPrev to the node before index jj
        while (jj > 0)
        {
            jPrev = jPrev->next;
            if (jPrev->next == NULL) // Return false if jj is out of bounds
                return false;
            jj--;
        }
        jCurr = jPrev->next;

        // Swap iCurr and jCurr
        tmp = jCurr->next;
        if (iCurr == jPrev) // Special case if iCurr and jCurr are adjacent
            jCurr->next = iCurr;
        else
        {
            jCurr->next = iCurr->next;
            jPrev->next = iCurr;
        }
        iCurr->next = tmp;
        iPrev->next = jCurr;

        return true;
    }
}
