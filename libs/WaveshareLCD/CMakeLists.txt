add_library(WaveshareLCD)

target_include_directories(WaveshareLCD
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_sources(WaveshareLCD
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/src/LCD_1in28.c
)

target_link_libraries(WaveshareLCD
    PUBLIC
        WaveshareConfig
)
