---
question: How does RIOT compare to other operating systems for embedded or IoT devices?
---

##### Disclaimer

Developing an OS for embedded systems involves many trade-offs.
Hence, there is not a single right choice for every application.
In this comparison we try to give a balanced comparison of the high-level architectural trade-offs other operating systems took and how they compare to RIOT.
Additionally, we compare the government of the project and the licensing.

##### RIOT

RIOT runs on many different CPU architectures by many different vendors, from [a tiny 8-bit MCU with 2 KiB RAM and 32 KiB flash][riot-arduino-nano] all the way up to high-performance [ARM Cortex M][riot-same54-xpro] and [RISC-V][riot-esp32c3-devkit] MCUs.
Because RIOT abstracts the hardware differences by providing the same API for the same functionality across this large range of MCUs, projects building upon RIOT are highly portable and therefore resilient to changes in the supply chain.

RIOT is designed to be a general-purpose OS with batteries included.
It provides a large collection of in-tree modules and out-of-tree packages that seamlessly integrate in your application.
This allows developers to pick the features they need from a large collection (as long as they can fit on the MCU).

RIOT aims to be easy to learn by using sane defaults, by providing good documentation, and via its helpful community that happily answers questions [in the forum][riot-forum] or in the [matrix chat][riot-matrix].
However, RIOT does not sacrifice advanced features, productivity or the ability to tinker with settings for more simplicity.
This makes RIOT suitable for students in teaching, tinkerers in the DIY community, and professionals alike.

RIOT is developed by a diverse, open, and [self-governed][riot-community-process] community.
Members in the community mostly belong to one (or more) of the following groups: academia, industry, and makers/hobbyists.

RIOT is distributed under a copyleft license and strongly prefers free and open source components over proprietary code and binary blobs.
Still, RIOT does contain proprietary drivers (some even using binary blobs) where no free alternative is available, e.g. for the ESP WiFi chipset.
<!-- FIXME: Make FAQ entries linkable and link to "Why LGPL?" -->

##### Vendor Specific SDKs

Most MCU vendors provide an SDK that is tied to and only supports MCUs of that specific vendor.
The advantage of the vendor SDKs is that they are developed in lock-step with the hardware and expose all features of the hardware early on.
The RIOT community can only start working on drivers once the MCUs are generally available and more exotic features that are only relevant to niche use cases may never be supported in favor of a cleaner and more portable API in RIOT.

From a governance point of view, RIOT is developed by a self-governed community, while the vendor SDKs are under tight control of the vendor.
Because of that, the RIOT community has maintained many popular boards well after the vendors declared them obsolete, while vendor SDKs often phase out support for older MCUs sooner.

Vendor specific SDKs typically do not have any copyleft clauses.

##### Arduino

Both RIOT and [Arduino][arduino-homepage] have a strong focus on a gentle learning curve and a low entry barrier.
Arduino however goes a step further and sacrifices advanced features such as native multi-threading, a full-fledged and mature network stack, or a VFS subsystem for simplicity.
This combined with a trimmed-down IDE results in a lower entry barrier for Arduino compared to RIOT.

RIOT still allows new users to quickly get productive, but without limiting developers to specific design patterns, specific software architectures, and a strong tie to a specific IDE.
As a nice treat for users that started with Arduino but ran into limitations, our [Arduino compatibility layer][riot-arduino] allows re-using sketches and libraries from the Arduino world.

Arduino has a vast ecosystem of libraries developed independently by third parties.
The number of modules and packages shipped with RIOT is smaller, but they are seamlessly integrated, provide a consistent API and combine well with each other.
This results in easier reuse of code and higher productivity without having to worry about interoperability issues of components and "impedance matching" between misaligned APIs.

The Arduino software is released under a copyleft license and hardware support can be extended greatly beyond the official Arduino boards by using third-party Arduino cores.
The development of the ecosystem is sponsored and controlled by a single company that owns the registered trademark of Arduino, while with RIOT an [independent community][riot-community-process] is responsible for governance.

##### Zephyr

[Zephyr][zephyr-homepage] has a larger and more complex code base, a very sophisticated configuration system, and unique tooling and is backed by a larger community than RIOT.
This results in a larger feature set at the expense of a steeper learning curve.

RIOT's leaner code base makes the code easier to understand and results in a lower memory footprint.
In addition, RIOT has been ported to 8-bit and 16-bit platforms, allowing its use on MCUs that are too resource constrained to run Zephyr.

Zephyr's larger code base and development community does give Zephyr an edge when it comes to the number of features supported.
We do believe that RIOT has an edge over Zephyr when a gentle learning curve, memory consumption, or quick prototyping cycles are priorities.

Zephyr uses a permissive license and is developed by the Linux Foundation.
Its development is governed by a [technical steering committee][zephyr-tsc] elected from (paying) members, whereas RIOT is steered by a [self-governed community][riot-community-process].

##### FreeRTOS / FreeRTOS for AWS IoT

[FreeRTOS][freertos-homepage] focuses on the basic core-OS features such as a scheduler and a small set of libraries.
This clear focus resulted in FreeRTOS being ported to more platforms than RIOT, despite its smaller development community.

RIOT on the other hand packs a lot more features as seamlessly integrated as modules and packages.
The ability to quickly enable and build upon these features reduces the development time needed for a certain application.

[FreeRTOS for AWS IoT][freertos-aws-homepage] provides libraries that ease the use of cloud APIs offered by a certain service provider from microcontrollers.
RIOT on the other hand is open minded about the network architecture and enables applications developers to choose freely:
RIOT can communicate with centralized cloud services (without any preference on the service provider), use a centralized on-premise architecture, use decentralized machine-to-machine communication, or operate offline.

FreeROTS and FreeRTOS for AWS IoT are both developed by Amazon Web Services, Inc. under a permissive license.

##### Contiki-NG

[Contiki-NG][contiki-ng-homepage] has a smaller development community and a small and focused code base.
It has a strong focus on research, whereas RIOT intents to be a general-purpose OS.
A unique feature of Contiki-NG is the Cooja Network Simulator.
RIOT provides similar simulation features with the [ZEP packet dispatcher][riot-zep-dispatcher], but clearly Cooja is a more tightly integrated and polished experience.
Another aspect where Contiki-NG's focus on research manifests is that Contiki-NG only supports a small number of boards, while having a quite sophisticated network stack.

As a result of the larger and more active community, RIOT packs more features, has a faster development pace, supports more MCU families, and has been ported to far more boards.
While Contiki-NG's network simulator and small code base make it a strong competitor to RIOT in the domain of research, RIOT has a clear edge over Contiki-NG when it comes to the hardware support and the features required for many real world applications.

Contiki-NG's development is steered by a small group of (mostly) computer science researchers and it is distributed under a permissive license.

<!-- Links, sorted alphabetically: -->
[arduino-homepage]: https://www.arduino.cc
[contiki-ng-homepage]: https://www.contiki-ng.org/
[freertos-aws-homepage]: https://www.freertos.org/iot-libraries.html
[freertos-homepage]: https://www.freertos.org
[riot-arduino-nano]: https://doc.riot-os.org/group__boards__arduino-nano.html
[riot-arduino]: https://doc.riot-os.org/group__sys__arduino.html
[riot-community-process]: https://doc.riot-os.org/community-processes.html
[riot-espc3-devkit]: https://doc.riot-os.org/group__boards__esp32c3__devkit.html
[riot-forum]: https://forum.riot-os.org
[riot-matrix]: https://matrix.to/#/#riot-os:matrix.org
[riot-same54-xpro]: https://doc.riot-os.org/group__boards__same54-xpro.html
[riot-zep-dispatcher]: https://github.com/RIOT-OS/RIOT/tree/master/dist/tools/zep_dispatch
[zephyr-homepage]: https://www.zephyrproject.org
[zephyr-tsc]: https://www.zephyrproject.org/wp-content/uploads/sites/38/2020/09/CLEAN-LF-Zephyr-Charter-20200624-effective-20200901.pdf
