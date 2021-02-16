---
question: How much memory (ROM/RAM) will it need?
---

This depends on the board and on the application. When you compile an application for a board, the last thing printed gives each sections memory footprint and looks like this:
```
    text       data     bss     dec     hex filename
    77732     296   24272  102300    18f9c applications/sixlowapp/bin/iot-lab_M3/sixlowapp.elf
```
The required RAM is `data + bss`, ROM is `text + data`.

**Please note:** Usually a big portion of RAM is consumed by the stack space for threads. Although RIOT maintainers try to optimize the default values, manual tweaking may be necessary to get the most efficient results. You can check the maximum stack usage at runtime with the shell command `ps` or the corresponding function `thread_print_all()` from the module `ps`.
