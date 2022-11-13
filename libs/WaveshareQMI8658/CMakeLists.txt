add_library(WaveshareQMI8658)

target_include_directories(WaveshareQMI8658
                           PUBLIC ${CMAKE_CURRENT_LIST_DIR}/include)

target_sources(WaveshareQMI8658 PUBLIC ${CMAKE_CURRENT_LIST_DIR}/src/QMI8658.c)

target_link_libraries(WaveshareQMI8658 PUBLIC WaveshareConfig)
