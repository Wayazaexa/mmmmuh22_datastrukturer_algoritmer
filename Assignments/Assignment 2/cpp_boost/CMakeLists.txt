cmake_minimum_required(VERSION 3.14 FATAL_ERROR)
project(FileCrawler)


# work-around: FindBoost: Boost_ARCHITECTURE not detected on MinGW
# https://gitlab.kitware.com/cmake/cmake/-/issues/20587
if(MINGW)
    if (CMAKE_SIZEOF_VOID_P EQUAL 8)
        set(Boost_ARCHITECTURE "-x64")
    else()
        set(Boost_ARCHITECTURE "-x32")
    endif()
endif()

# works with/without
set(Boost_USE_STATIC_LIBS ON)

set(Boost_DEBUG ON)



find_package(Boost
    COMPONENTS
    system
    filesystem
    REQUIRED) # just an example, add what you need

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -w")

# ---- Create binary ----
include_directories(${Boost_INCLUDE_DIRS})

## Set your file here
add_executable(FileCrawler file_handling_example.cpp)

target_compile_features(FileCrawler PRIVATE cxx_std_17)

target_link_libraries(FileCrawler  ${Boost_LIBRARIES})
