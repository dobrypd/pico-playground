# RP2040 watch

Watch application for
Raspberry Pi Pico RP2040, with 1.28" 240x240 LCD display. Like [this one](https://www.spotpear.com/index.php/index/study/detail/id/761.html).

## How to build

Project depends on `pico-sdk` and uses `cmake` as build system.

### Dependencies
 - [pico-sdk](https://github.com/raspberrypi/pico-sdk)

```export PICO_SDK_PATH=(the path to SDK)```

### Build

- Configure project, ie.:
```bash
$ mkdir build
$ cd build
$ cmake ..
```
- Build
```bash
$ make -j $(nproc --all)
```
