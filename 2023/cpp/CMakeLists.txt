cmake_minimum_required(VERSION 3.0)
project(aoc2023 VERSION 1.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)

add_compile_options(-Wall -O3)
add_subdirectory(src)
add_executable(aoc src/aoc.cpp)
target_link_libraries(aoc PRIVATE solvers)
target_include_directories(aoc PRIVATE ${PROJECT_SOURCE_DIR}/include/solvers)
