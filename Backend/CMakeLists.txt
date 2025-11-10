cmake_minimum_required(VERSION 3.27)
project(Backend)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(nlohmann_json REQUIRED)
message(STATUS "nlohmann found")

find_package(GTest REQUIRED)
message(STATUS "GTest found")

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME}
        PRIVATE
        nlohmann_json::nlohmann_json
        GTest::gtest
        GTest::gmock
        GTest::gtest_main
        GTest::gmock_main
)

target_include_directories(${PROJECT_NAME} PRIVATE
        ${nlohmann_json_INCLUDE_DIRS}
        ${GTest_INCLUDE_DIRS}
)