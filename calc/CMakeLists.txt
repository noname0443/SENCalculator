# CMakeList.txt: файл проекта CMake верхнего уровня; проведите глобальную конфигурацию
# и включите сюда подпроекты.

cmake_minimum_required(VERSION 3.8)
project(calc VERSION 0.1.0 DESCRIPTION "rgncls")
include(GNUInstallDirs)
add_library(${PROJECT_NAME} SHARED
    sources/calculator.c
    sources/stack.c
    sources/token.c
    sources/export.c
    include/exeptions.h
    include/calcresult.h)
set_target_properties(${PROJECTNAME} PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    PUBLIC_HEADER include/export.h)
configure_file(calc.pc.in calc.pc @ONLY)
target_include_directories(calc PRIVATE .)
install(TARGETS calc
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${CMAKE_BINARY_DIR}/calc.pc
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)