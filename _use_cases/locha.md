---
project: Chat and send Bitcoin without Internet
quote: In Locha Mesh, we decided to use RIOT for a variety of reasons, including an active community surrounding it, the overall design of the Operating System that's coupled with a powerful and extensible network stack, and the support for a good variety of CPUs and boards.
user: Jean Pierre Dudey
user_position: Embedded Software Developer
user_photo: user-photos/Jean-Pierre-Dudey.jpg
company: Locha Mesh
company_logo: logos/lochamesh-logo.svg
company_url: https://locha.io
---

## About

Locha Mesh develops an alternative and resilient data transmission technology for mobile communications and payments without having to rely on an Internet connection, using the mesh network topology AODVv2 to enable direct P2P connections between nodes. The Locha Mesh has full IPv6 support so most of the current applications can run on it.

## Why RIOT?

### Easy to use.

Using RIOT has allowed us to easily extend the network stack to support an external routing protocol as it provides a good base to work with, to build a system from the ground up.

When searching for other embedded Operating Systems not much of them had a good documentation as RIOT has. This was critical for the initial design of the code. Other OS abstractions for network interfaces didn't provide us the extensibility we wanted to add a custom routing protocol. 

### Low memory footprint.
Other consideration we had is how much the OS would take in flash and RAM. In this case RIOT performed excellently because you pay only for what you use, code that is not necessary for the correct working of the firmware doesn't get compiled, giving more room for the firmware to be improved.

### Modular network stack.
The way RIOT GNRC stack is designed allowed us to write the routing protocol in a network interface independent way, and while our main goal is using IPv6 over IEEE 802.25.4 (6LoWPAN) it doesn't lock us to a single network interface, so that changing from IEEE 802.15.4 to Ethernet or WiFi doesn't take more than changing some lines of code to select what we want to use, without touching the routing protocol. This coupled with the variety of supported boards and CPUs allowed us to not get locked to a single vendor of hardware.

### Sound contribution processes.
The most notable thing about RIOT is the community and maintainers which have been helpful all the way along for the review of patches to add support for our hardware, device drivers, etc. In short terms, the contributing process is very good and welcoming for external contributors.

