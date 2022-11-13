add_library(STMicroelectronicsFonts)

target_include_directories(STMicroelectronicsFonts
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_sources(STMicroelectronicsFonts
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include/Fonts/fonts.h
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/font8.c
        ${CMAKE_CURRENT_LIST_DIR}/src/font12.c
        ${CMAKE_CURRENT_LIST_DIR}/src/font16.c
        ${CMAKE_CURRENT_LIST_DIR}/src/font20.c
        ${CMAKE_CURRENT_LIST_DIR}/src/font24.c
)
