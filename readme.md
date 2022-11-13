# Raspberry Pi Pico watch playground

Watch application playground for
Raspberry Pi Pico RP2040, with 1.28" 240x240 LCD display. Like [this one](https://www.spotpear.com/index.php/index/study/detail/id/761.html).

* Microcontroller RP2040
* LCD display GC9A01A
* IMU QMI8658C

## How to build

Project depends on `pico-sdk` and uses `cmake` as build system.

### Dependencies
 - [pico-sdk](https://github.com/raspberrypi/pico-sdk)

```export PICO_SDK_PATH=(the path to SDK)```

### Build

- Configure the project with cmake, ie.:
```bash
$ mkdir build
$ cd build
$ cmake ..
```
- Build it
```bash
$ make -j $(nproc --all)
```

## Development

### Create environment

```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r dev_tools/requirements.txt
```

#### Source code formatting

```bash
$ python dev_tools/format.py --repo_root `pwd`
```
