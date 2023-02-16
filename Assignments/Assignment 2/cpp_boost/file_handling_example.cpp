#include <iostream> // To read user input
#include <string>

// Boost file handling
#include <boost/filesystem.hpp>
#include <boost/filesystem/fstream.hpp>

#include <unordered_map> // For bonus exercise
#include <bits/stdc++.h> // For bonus exercise, string manipulation

using namespace boost::filesystem;

int main()
{
    std::string search_path = "../TestData";

    if (is_directory(search_path))
    {
        std::cout << "./TestData is a directory" << std::endl;
    }

    if (!is_regular_file(search_path))
    {
        std::cout << "Hence it is not a regular file" << std::endl;
    }

    // List directories and files in directory TestData:
    path p;
    for (directory_iterator itr(search_path); itr != directory_iterator(); ++itr)
    {
        if (itr->path().filename() != "." && itr->path().filename() != "..")
        {
            p = itr->path();
            std::cout << p.string() << std::endl;
        }
    }

    // If last file is a regular file, print its content
    if (is_regular_file(p)) {
        ifstream file(p.string());
        std::string line;
        while (getline(file, line)) {
            // Print the line. In the assignment, you rather want to search in the string.
            std::cout << line << std::endl;
        }
    }

}