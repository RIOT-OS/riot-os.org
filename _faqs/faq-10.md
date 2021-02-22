---
question: Does RIOT support Raspberry PI?
---

No. From the RIOT point of view the Raspberry PI is a supercomputer. RIOT targets mostly systems that are too constrained to run Linux (less than 1MB of RAM, no MMU). However, it is supported to run [RIOT native](https://github.com/RIOT-OS/RIOT/wiki/Family:-native) on platforms like the Raspberry PI, and other hardware supported by Linux or BSD.

A good rule of thumb concerning RIOT support of a particular board is: can Linux support this board? If yes, then you should ask yourself *why* you really want to use RIOT (other than [native](https://github.com/RIOT-OS/RIOT/wiki/Family:-native)) on this board. If no, then RIOT support is probably desirable.

