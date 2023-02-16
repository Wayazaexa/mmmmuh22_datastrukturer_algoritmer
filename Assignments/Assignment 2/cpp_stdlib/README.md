# C++ version of assignment 2

There are numerous ways you can open and read files in C++. Here is an example of some file handling using standard library. 

Note: I have not fixed handling of file encodings (å, ä, ö) which is rather tricky with C++. It is ok that you don't handle this in the assignment as well :)

## Alter CMakeLists.txt
Change this line:

```
add_executable(FileCrawler file_handling_example.cpp)
```

To your file. You might add multiple files.

## Build and run

First create build files (usually only needed once, or if new files are added):

```
cmake -S . -B build
``` 

Then build it:

```
cmake --build build
``` 

Then run:

```
./build/FileCrawler.exe
``` 

