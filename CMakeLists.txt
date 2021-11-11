# minimum CMake version required
cmake_minimum_required(VERSION 3.15)
# Project name, version and description
project(DiscordSchoolity VERSION 1.0 DESCRIPTION "A discord bot that interacts with the Schoolity software")
 
# Add DPP as dependency
add_subdirectory(libs/DPP)
add_subdirectory(src/headers/) 
# Create an executable
add_executable(${PROJECT_NAME}
    src/main.cpp
    # your others files...
)
 
# Linking libraries
target_link_libraries(${PROJECT_NAME}
    dpp
    spdlog # if you need a logger. Don't forget to clone sources
           # in the `libs/` directory
)
 
# Specify includes
target_include_directories(${PROJECT_NAME} PRIVATE
    libs/DPP/include
    libs/spdlog/include # Like before, if you need spdlog
)
 
# Set C++ version
set_target_properties(${PROJECT_NAME} PROPERTIES
    CXX_STANDARD 17 # or 20 if you want something more recent
    CXX_STANDARD_REQUIRED ON
)

