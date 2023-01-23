
#include <iostream>
#include "storage.hh"

int main()
{
    Storage *s = new Storage();
    std::cout << std::boolalpha;
    std::cout << "isEmpty? " << s->isEmpty() << "\n";
    s->push(1);
    s->push(2);
    s->push(3);
    s->push(4);
    s->push(5);
    int pop;

    if (s->swap(1, 4))
        std::cout << "Swap successful!\n";
    else
        std::cout << "Swap failed!\n";

    if (s->pop(pop))
        std::cout << pop << "\n";
    if (s->peek(pop))
        std::cout << "Peeking: " << pop << "\n";
    std::cout << "isEmpty? " << s->isEmpty() << "\n";
    if (s->pop(pop))
        std::cout << pop << "\n";
    if (s->pop(pop))
        std::cout << pop << "\n";
    if (s->pop(pop))
        std::cout << pop << "\n";
    if (s->pop(pop))
        std::cout << pop << "\n";
    std::cout << "isEmpty? " << s->isEmpty() << "\n";
    if (s->pop(pop))
        std::cout << pop << "\n";
    std::cout << "\n";

    return 0;
}
