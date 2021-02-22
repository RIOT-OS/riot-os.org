---
question: Why LGPL?
---

Studies such as [this one](http://www.gartner.com/newsroom/id/2869521) show that small companies and start-ups are going to determine IoT. More than bigger companies, such small structures need to spread development and maintenance costs for the kernel and all the software that is not their core business. Our analysis is that this is more compatible with LGPL than with BSD/MIT.

We are of the opinion that, compared to BSD/MIT, LGPL will improve final user experience, security and privacy, by hindering device lock-down, favoring up-to-date, and field-upgradable code. We think this a more solid base to provide a consistent, compatible, secure-by-default standard system which developers can build upon to create trustworthy IoT applications, while not hindering business models based on closed source linked with RIOT (see the [automated tools](https://github.com/RIOT-OS/RIOT/tree/master/examples/bindist) provided to help check LGPL compliance, and/or [this technical guide](https://github.com/RIOT-OS/RIOT/wiki/LGPL-compliancy-guide))

Since solutions competing with RIOT are quasi-exclusively BSD/MIT, we gauge that LGPL is a way to stand out favorably, and is a characteristic backing positive comparisons of RIOT with Linux.

Last but not least, we think that (L)GPL is a better base than BSD/MIT to keep the community united in the mid and long run.

For the record: we have also considered MIT/BSD (see [this thread](https://lists.riot-os.org/pipermail/devel/2014-December/001468.html)), but there was not enthusiastic majority supporting such a switch.

Compare https://github.com/RIOT-OS/RIOT/issues/2128
