#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>

#include <unordered_map> // For bonus exercise
#include <bits/stdc++.h> // For bonus exercise, string manipulation


using namespace std;
namespace fs = std::filesystem;

int main()
{
    std::string search_path = "../TestData";

    if (fs::is_directory(search_path))
    {
        std::cout << "./TestData is a directory" << std::endl;
    }

    if (!fs::is_regular_file(search_path))
    {
        std::cout << "Hence it is not a regular file" << std::endl;
    }

    // List directories and files in directory TestData:
    fs::path p;
    for (fs::directory_iterator itr(search_path); itr != fs::directory_iterator(); ++itr)
    {
        if (itr->path().filename() != "." && itr->path().filename() != "..")
        {
            p = itr->path();
            std::cout << p.string() << std::endl;
        }
    }

    // If last file is a regular file, print its content
    if (fs::is_regular_file(p) && !p.empty())
    {
        std::ifstream file(p.string());
        std::string line;
        while (std::getline(file, line))
        {
            // Print the line. In the assignment, you rather want to search in the string.
            std::cout << line << std::endl;
        }
    }

}
