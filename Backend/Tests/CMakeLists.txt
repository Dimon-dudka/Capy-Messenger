find_package(GTest REQUIRED)
if (GTest_FOUND)
    message(STATUS "GTest found: ${GTest_VERSION}")
else ()
    message(FATAL_ERROR "GTest was not found")
endif ()

add_executable(backend_tests
        test_main.cpp
)

target_link_libraries(backend_tests
        PRIVATE
        backend_lib
        GTest::gtest
        GTest::gtest_main
)