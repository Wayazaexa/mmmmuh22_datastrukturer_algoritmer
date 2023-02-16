# C++ version of assignment 2

There are numerous ways you can open and read files in C++. The example I add is using boost file handling library. I add CMake file to help you build it with boost.

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

