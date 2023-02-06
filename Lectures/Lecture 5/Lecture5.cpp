#include <iostream>

using namespace std;

template <typename T, size_t n>
void print_array(T const (&arr)[n])
{
    for (size_t i = 0; i < n; i++)
    {
        std::cout << arr[i] << ' ';
    }
}

/**
 * Gör en linjär sökning i en icke-sorterad array
 *
 * sizeof fungerar inte när vi skickar array som parameter,
 * måste ha extra paramter in i funktionen
 *
 * Returnerar -1 om objektet inte hittas
 */
int linear_search(int unsorted_array[], size_t size, int item)
{
    for (int i = 0; i < size; i++)
    {
        if (unsorted_array[i] == item)
        {
            return i;
        }
    }
    return -1;
}

/**
 * Gör en sökning i en array som är sorterad
 */
int binary_search(int sorted_array[], size_t size, int item)
{
    int first = 0;
    int last = size - 1;
    int midpoint;

    while (first <= last)
    {
        midpoint = (last + first) / 2;
        if (item == sorted_array[midpoint])
        {
            // Vi har hittat den!
            return midpoint;
        }
        else if (item < sorted_array[midpoint])
        {
            // Släng högersidan
            last = midpoint - 1;
        }
        else if (item > sorted_array[midpoint])
        {
            // Släng vänstersidan
            first = midpoint + 1;
        }
    }
    // Vi hittade den inte!
    return -1;
}

/**
 * Sorterar lista genom bubble sort
 * modifierar listan!
*/
void bubble_sort(int unsorted_list[], size_t size) {
    int compare_count = 0;

    for (int i = 0; i<size-1; i++) {
        bool swapped = false;
        for (int j = 0; j<size-i-1; j++) {
            compare_count++;
            if (unsorted_list[j]>unsorted_list[j+1]) {
                int tmp = unsorted_list[j];
                unsorted_list[j] = unsorted_list[j+1];
                unsorted_list[j+1] = tmp;
                swapped = true;
            }
        }
        if (!swapped) {
            // Om vi inte gjort någon swap är listan redan sorterad
            break;
        }
    }
    cout << "Compare count: " << compare_count << endl;
}

int main()
{
    int unsorted_list[] = {4, 5, 1, 2, 15, 7};
    cout << "Unsorted list: ";
    print_array(unsorted_list);
    cout << endl;
    cout << "Index of element 2: " << linear_search(unsorted_list, 6, 2) << endl;
    cout << "Index of element 22: " << linear_search(unsorted_list, 6, 22) << endl;

    int sorted_list2[] = { 1, 2, 7, 9, 12, 13, 17, 21, 22 };
    cout << "Sorted list 2: ";
    print_array(sorted_list2);
    cout << endl << "Index of element 13: " << binary_search(sorted_list2, sizeof(sorted_list2)/sizeof(sorted_list2[0]), 13);
    cout << endl << "Index of element 14: " << binary_search(sorted_list2, sizeof(sorted_list2)/sizeof(sorted_list2[0]), 14) << endl;

    int sorted_list3[] = {-14, -8, -7, 0, 2, 7, 21};
    cout << "Sorted list 3: ";
    print_array(sorted_list3);
    cout << endl << "Index of element -11: " << binary_search(sorted_list3, sizeof(sorted_list3)/sizeof(sorted_list3[0]), -11) << endl;

    bubble_sort(unsorted_list, 6);
    cout << "After sorting unsorted list: ";
    print_array(unsorted_list);
    cout << endl;

    int unsorted_list2[] = {5, 4, 3, 2, 1, 0, -1};
    cout << "Unsorted list 2" << endl;
    print_array(unsorted_list2);
    cout << endl;
    bubble_sort(unsorted_list2, sizeof(unsorted_list2)/sizeof(unsorted_list2[0]));
    cout << "After sorting unsorted list2: ";
    print_array(unsorted_list2);
    cout << endl;
    int unsorted_list3[] = {8, 7, 1, 2, 3, 4, 5, 6};
    cout << "Unsorted list 3" << endl;
    print_array(unsorted_list3);
    cout << endl;
    bubble_sort(unsorted_list3, sizeof(unsorted_list3)/sizeof(unsorted_list3[0]));
    cout << "After sorting unsorted list3: ";
    print_array(unsorted_list3);
    cout << endl;

}