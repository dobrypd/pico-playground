add_library(WaveshareGUI)

target_include_directories(WaveshareGUI
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_sources(WaveshareGUI
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include/GUI_Paint.h
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/GUI_Paint.c
)

target_link_libraries(WaveshareGUI
    PUBLIC
        STMicroelectronicsFonts
        WaveshareConfig
)
