cmake_minimum_required(VERSION 3.27)
project(Backend)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(ENABLE_TESTS "Enable tests" ON)

if (ENABLE_TESTS)
    add_compile_definitions(ENABLE_TESTS)
endif ()

#------------------------------------------------------


#------------------------------------------------------
# setup test layout shared library
#------------------------------------------------------
add_subdirectory(Core)
#------------------------------------------------------


#------------------------------------------------------
# Main module setup
#------------------------------------------------------
add_executable(${PROJECT_NAME} main.cpp)
#------------------------------------------------------


#------------------------------------------------------
# Testing part
#------------------------------------------------------
if (ENABLE_TESTS)
    set(TESTS_FOLDER Tests)
    
    enable_testing()
    add_subdirectory(${TESTS_FOLDER})
endif ()