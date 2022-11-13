add_library(WaveshareConfig)

target_include_directories(WaveshareConfig
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_sources(WaveshareConfig
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include/Debug.h
        ${CMAKE_CURRENT_LIST_DIR}/include/DEV_Config.h
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/DEV_Config.c
)

target_link_libraries(WaveshareConfig
    PUBLIC
        pico_stdlib
        hardware_spi
        hardware_i2c
        hardware_pwm
        hardware_adc
)
