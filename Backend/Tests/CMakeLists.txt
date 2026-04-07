find_package(GTest REQUIRED)
if (GTest_FOUND)
    message(STATUS "GTest found: ${GTest_VERSION}")
else ()
    message(FATAL_ERROR "GTest was not found")
endif ()

add_executable(backend_tests
        test_main.cpp
        Core/Ports/Secondary/Logger/LoggerMessageTestsClass.cpp
        Core/Ports/Secondary/Logger/LoggerMessageTestsClass.h
        Utils/Exceptions/BaseFormattedExceptionTests.h
        Utils/Exceptions/BaseFormattedExceptionTests.cpp
)

target_link_libraries(backend_tests
        PRIVATE
        backend_core_lib
        utils_lib
        GTest::gtest
        GTest::gtest_main
)