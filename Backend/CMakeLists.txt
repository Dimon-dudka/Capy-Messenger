cmake_minimum_required(VERSION 3.27)
project(Backend)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(TESTS_FOLDER Tests)


#------------------------------------------------------
# nlohmann include
#------------------------------------------------------
find_package(nlohmann_json REQUIRED)
if (nlohmann_json_FOUND)
    message(STATUS "nlohmann found")
else ()
    message(FATAL_ERROR "nlohmann was not found")
endif ()
#------------------------------------------------------


#------------------------------------------------------
# setup test layout shared library
#------------------------------------------------------
add_library(backend_lib OBJECT
        TestLayout/TestClass.h
        TestLayout/TestClass.cpp
)

target_link_libraries(backend_lib
        PRIVATE
        nlohmann_json::nlohmann_json
)
#------------------------------------------------------


#------------------------------------------------------
# Main module setup
#------------------------------------------------------
add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME}
        PRIVATE
        backend_lib
)

target_include_directories(${PROJECT_NAME} PRIVATE
        ${nlohmann_json_INCLUDE_DIRS}
)
#------------------------------------------------------


#------------------------------------------------------
# Testing part
#------------------------------------------------------
enable_testing()
add_subdirectory(${TESTS_FOLDER})