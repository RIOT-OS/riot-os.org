---
question: (Why) is there no 64 bit support, at least in native?
---

There is not much to be gained from 64 bit support as RIOT does not target any other platforms that offer 64 bit.
That being said there are pros and cons.

Pro:
- improve RIOT's code base by fixing 64 bit related errors
- simplify toolchain setup for native

Con:
- effort / gain (as it's unlikely we will support any other 64 bit platform, fixing potential 64 bit errors in RIOT is less beneficial)
- decreased 32 bit testing (unless we make 32 the default in which case the toolchain setup argument is diminished)

From our perspective this does not justify pulling manpower from other tasks. Nobody will stop you from adding support if you want to, though ;)

See also: https://github.com/RIOT-OS/RIOT/issues/6603
