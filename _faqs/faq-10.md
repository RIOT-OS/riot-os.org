---
question: Does RIOT support Raspberry Pi?
---

RIOT does support the [Raspberry Pi Pico](https://doc.riot-os.org/group__boards__rpi__pico.html) and the [Raspberry Pi Pico W](https://doc.riot-os.org/group__boards__rpi__pico__w.html).

The Linux-capable Raspberry Pi boards are not supported, though. From the RIOT point of view these boards are supercomputers. RIOT targets mostly systems that are too constrained to run Linux (less than 1MB of RAM, no MMU). However, it is supported to run [RIOT native](https://doc.riot-os.org/group__boards__native.html) ([or the 64 bit native variant](https://doc.riot-os.org/group__boards__native64.html)) on platforms like the Raspberry Pi, and other hardware supported by Linux.

A good rule of thumb concerning RIOT support of a particular board is: can Linux support this board? If yes, then you should ask yourself *why* you really want to use RIOT (other than [native](https://doc.riot-os.org/group__boards__native.html)) on this board. If no, then RIOT support is probably desirable.
