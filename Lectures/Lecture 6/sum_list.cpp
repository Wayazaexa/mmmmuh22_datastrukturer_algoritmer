#include <vector>
#include <iostream>

using namespace std;


int sum_list(vector<int> myVector) {
    if (myVector.size()==0) {
        return 0;
    }
    return myVector.front() + sum_list({myVector.begin()+1, myVector.end()});
}

int sum_list_array(int myArr[], unsigned int n) {
    if (n==0) {
        return 0;
    }
    return myArr[0] + sum_list_array(&myArr[1], n-1);
}

int main() {
    vector<int> myVector = {5, 4, 2, 7, 1};
    cout << "Sum of list (vector): " << sum_list(myVector) << endl;

    int n = 5;
    int myArray[] = {5, 4, 2, 7, 1};
    cout << "Sum of list (array): " << sum_list_array(myArray, n) << endl;
}