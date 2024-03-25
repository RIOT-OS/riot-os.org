---
question: What is the benefit of RIOT compared to bare metal programming?
---

In short: Increased productivity.

RIOT provides a number of features that make reusing code easier:
In RIOT hardware is abstracted by vendor-agnostic driver APIs and multi-threading eases decoupling of the implementation of distinct features.
Particularly helpful is RIOT's module system, that also allows seamless integration of external modules.

In addition RIOT already provides a lot of functionality that is ready for use, such as modules providing a network stack, network protocols, and large number of device drivers.
This can cut down development time significantly compared to bare metal programming.
