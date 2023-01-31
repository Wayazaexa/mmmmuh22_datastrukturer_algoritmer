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
    std::cout << s << "\n";
    int pop;

    s->swap(-1, 3); // Should fail
    std::cout << s << " failed swap?\n";
    s->swap(1, 3);
    std::cout << s << "\n";
    s->swap(0, 3);
    std::cout << s << "\n";
    s->swap(1, 6); // Should fail
    std::cout << s << " failed swap?\n";
    if (s->swap(1, 2))
        std::cout << "Swap successful!\n";
    else
        std::cout << "Swap failed!\n";
    std::cout << s << "\n";

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
    std::cout << s << "\n";
    std::cout << "\n";

    return 0;
}
