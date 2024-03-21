---
question: How does RIOT compare to XYZ?
---

Compared to **vendor specific solutions**, RIOT runs on many different CPU architectures by many different vendors, from a tiny 8-bit MCU with 2 KiB RAM and 32 KiB flash all the way up to high performance ARM Cortex M and RISC-V MCUs.
Because RIOT abstracts the hardware differences by providing the same API for the same functionality across this large range of MCUs, projects building upon RIOT are highly portable and therefore resilient to changes in the supply chain.

Compared to **Arduino**, RIOT provides advanced features such as native multi-threading and a mature network stack, while still providing a gentle learning curve.
This allows new users to quickly get productive with RIOT without limiting developers to specific design patterns and software architectures.
As a nice treat for users migrating from Arduino, our [Arduino compatibility layer](https://doc.riot-os.org/group__sys__arduino.html) allows re-using sketches and libraries from the Arduino world.

Compared to **zephyr**, RIOT is less complex and has a smaller code base.
This results in a more gentle learning curve and a shorter on-boarding time needed to get productive with RIOT.
In addition RIOT has a smaller memory footprint and has been ported to 8-bit and 16-bit platforms, allowing RIOT to be used on MCUs that are too resource constraint to run zephyr.
Zephyr's larger code base and development community does give zephyr an edge when it comes to the number of features supported.
We do believe that RIOT has an edge over zephyr when a gentle learning curve, memory consumption, or quick prototyping cycles are priorities.

Compared to **FreeRTOS** which only provides the basic core OS features such a scheduler, RIOT packs many optional features seamlessly integrated as modules and packages.
The ability to quickly enable and build upon these features reduces the development time needed for a certain application.
FreeRTOS has an edge when it comes to the number of architectures supported, though.

Compared **a:FreeRTOS**, RIOT is open minded about the network architecture and gives you all the choices.
That is, while RIOT can communicate with cloud services (without any preference on the service provide), you can just as well opt for direct machine to machine communication, on-premise architectures, or offline applications without network connectivity.

Compared to **Contiki-NG**, RIOT has a larger, more active community.
As a result, RIOT packs more features, has a faster development pace, supports more MCUs families, and has been ported to far more boards.
While the tiny codebase of Contiki-NG allows to quickly get a thorough understanding, RIOT has a clear edge over Contiki-NG when it comes to the hardware support and the features required for many real world applications.
