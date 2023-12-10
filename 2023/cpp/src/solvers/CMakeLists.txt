add_library(solvers 
    registry.cpp
    solution.cpp
    d01.cpp
)
target_include_directories(solvers PRIVATE ${PROJECT_SOURCE_DIR}/include/solvers)
