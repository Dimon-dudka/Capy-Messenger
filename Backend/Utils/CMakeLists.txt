SET(UTILS_LIB_NAME "utils_lib")

#------------------------------------------------------

add_library(${UTILS_LIB_NAME} OBJECT
        Exceptions/BaseFormattedException.h
)


target_include_directories(${UTILS_LIB_NAME}
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/Exceptions
)