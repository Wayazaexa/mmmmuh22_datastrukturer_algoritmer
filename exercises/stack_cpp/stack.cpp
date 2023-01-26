#include <iostream>
#include <vector>
#include <string>

class Stack
{
private:
    std::vector<std::string> stack;
public:
    Stack(/* args */);
    ~Stack();

    void push(std::string);
    std::string pop();
    bool is_empty();
    std::string peek();
    int size();
};

Stack::Stack(/* args */)
{
}

Stack::~Stack()
{
}

void Stack::push(std::string x)
{
    stack.push_back(x);
}

std::string Stack::pop()
{
    std::string tmp = stack.back();
    stack.pop_back();
    return tmp;
}

bool Stack::is_empty()
{
    return stack.size() == 0;
}

std::string Stack::peek()
{
    return stack.back();
}

int Stack::size()
{
    return stack.size();
}

int main()
{
    Stack myStack;
    std::cout << std::boolalpha;
    std::cout << "Empty? " << myStack.is_empty() << "\n";
    std::cout << "Pushing \"3\"\n";
    myStack.push("3");
    std::cout << "Pushing \"2\"\n";
    myStack.push("2");
    std::cout << "Pushing \"1\"\n";
    myStack.push("1");
    std::cout << "Peeking: " << myStack.peek() << "\n";
    std::cout << "Size? " << myStack.size() << "\n";
    std::cout << "Popping: " << myStack.pop() << "\n";
    std::cout << "Popping: " << myStack.pop() << "\n";
    std::cout << "Empty? " << myStack.is_empty() << "\n";
    std::cout << "Size? " << myStack.size() << "\n";
    std::cout << "Popping: " << myStack.pop() << "\n";
    std::cout << "Empty? " << myStack.is_empty() << "\n\n";
    return 0;
}