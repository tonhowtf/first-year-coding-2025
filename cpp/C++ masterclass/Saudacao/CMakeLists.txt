cmake_minimum_required(VERSION 3.16)

project(Saudacao LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(Saudacao main.cpp)

include(GNUInstallDirs)
install(TARGETS Saudacao
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
