add_executable(watch
        watch.c
)

#target_link_libraries(main examples LCD QMI8658 GUI Fonts Config pico_stdlib   )
target_link_libraries(watch
        pico_stdlib
        hardware_i2c
        hardware_spi
        STMicroelectronicsFonts
        WaveshareConfig
        WaveshareGUI
        WaveshareLCD
        WaveshareQMI8658
)

# create map/bin/hex file etc.
pico_add_extra_outputs(watch)

# enable usb output, disable uart
pico_enable_stdio_usb(watch 1)
pico_enable_stdio_uart(watch 1)
