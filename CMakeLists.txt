cmake_minimum_required(VERSION 3.27)
project(Capy-Messenger)

if (DEFINED Python_EXECUTABLE OR DEFINED Python3_EXECUTABLE)
    message(STATUS "Python found at: ${Python_EXECUTABLE}${Python3_EXECUTABLE}")
endif ()

add_subdirectory(Backend)