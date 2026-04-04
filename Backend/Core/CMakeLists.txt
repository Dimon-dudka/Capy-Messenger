SET(BACKEND_CORE_LIB_NAME "backend_core_lib")

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

add_library(${BACKEND_CORE_LIB_NAME} OBJECT
        Ports/Secondary/Logger/Interfaces/BaseLoggerMessage.h
        Ports/Secondary/Logger/MessageTypes/TechLogMessage.cpp
        Ports/Secondary/Logger/MessageTypes/TechLogMessage.h
        Ports/Secondary/Logger/Utils/LoggerUtils.h
        Ports/Secondary/Logger/Utils/LoggerUtils.cpp
)

target_link_libraries(${BACKEND_CORE_LIB_NAME}
        PRIVATE
        nlohmann_json::nlohmann_json
)

target_include_directories(${BACKEND_CORE_LIB_NAME}
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/Ports/Primary
        ${CMAKE_CURRENT_SOURCE_DIR}/Ports/Secondary
        ${nlohmann_json_INCLUDE_DIRS}
)
