cmake_minimum_required(VERSION 3.22)

include(cmake/pico_sdk_import.cmake)

project(
  Pico_Watch
  VERSION 1.0.0
  LANGUAGES C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

if(PICO_SDK_VERSION_STRING VERSION_LESS "1.4.0")
  message(
    FATAL_ERROR
      "Raspberry Pi Pico SDK version 1.4.0 (or later) required. Your version is ${PICO_SDK_VERSION_STRING}"
  )
endif()
pico_sdk_init()

add_compile_options(
  -Wall -Wextra
  # -Wpedantic
)

add_subdirectory(libs)
add_subdirectory(apps)
