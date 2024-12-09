#
# Default data, only used when RIOTBASE is not provided or doesn't exist
#
DEFAULT_BOARDS = [
    { "name": "Arduino Duemilanove", "group": "arduino-duemilanove" },
    { "name": "Atmel SAM D10 Xplained Mini", "group": "samd10-xmini" },
    { "name": "MSB-IoT", "group": "msbiot" },
    { "name": "Native Board", "group": "native" },
    { "name": "Particle Xenon", "group": "particle-xenon" },
    { "name": "PineTime", "group": "pinetime" },
    { "name": "STM32 Nucleo-L4R5ZI", "group": "nucleo144-l4r5" },
    { "name": "STM32 Nucleo-L552ZE-Q", "group": "nucleo-l552ze-q" },
    { "name": "SiFive HiFive1 RISC-V board", "group": "hifive1" },
    { "name": "nRF52840-MDK", "group": "nrf52840-mdk" }

]
DEFAULT_CPUS = [
    { "group": "mips__pic32mz", "name": "PIC32MZ" },
    { "group": "nrf5x__common", "name": "Nordic nRF5x MCU" },
    { "group": "lm4f120", "name": "LM4F" },
    { "group": "esp32", "name": "ESP32" },
    { "group": "nrf5x__common", "name": "Nordic nRF5x MCU" },
    { "group": "samd21", "name": "Atmel SAMD10/SAMD20/SAMD21/SAMR21" },
    { "group": "sam3", "name": "Atmel SAM3" },
    { "group": "cc26x2__cc13x2", "name": "TI CC26x2, CC13x2" },
    { "group": "esp32", "name": "ESP32" },
    { "group": "lpc1768", "name": "NXP LPC1768" }
]
DEFAULT_DRIVERS = [
    {
        "name": "AT25xxx family of SPI-EEPROMs",
        "group": "at25xxx", "parent": "misc"
    },
    {
        "name": "SRF02 ultrasonic range sensor",
        "group": "srf02", "parent": "sensors"
    },
    {
        "name": "KW2x radio-driver",
        "group": "kw2xrf", "parent": "netdev"
    },
    {
        "name": "DFPlayer Mini MP3 Player",
        "group": "dfplayer", "parent": "multimedia"
    },
    {
        "name": "Pulse counter",
        "group": "pulse__counter", "parent": "sensors"
    },
    {
        "name": "ADXL345 3-Axis accelerometer",
        "group": "adxl345", "parent": "sensors"
    },
    {
        "name": "INA3221 current/power monitor",
        "group": "ina3221", "parent": "sensors"
    },
    {
        "name": "mtd wrapper for sdcard_spi",
        "group": "mtd__sdcard", "parent": "storage"
    },
    {
        "name": "Serial NOR flash",
        "group": "mtd__spi__nor", "parent": "storage"
    },
    {
        "name": "L3G4200D gyroscope",
        "group": "l3g4200d", "parent": "sensors"
    }

]
DEFAULT_DRIVER_CATEGORIES = [
    { "name": "Miscellaneous Drivers", "group": "misc" },
    { "name": "Multimedia Device Drivers", "group": "multimedia" },
    { "name": "Network Device Drivers", "group": "netdev" },
    { "name": "Sensor Device Drivers", "group": "sensors" },
    { "name": "Storage Device Drivers", "group": "storage" }
]
DEFAULT_CONTRIBUTORS = [
    {
        "login": "miri64",
        "avatar_url": "https://avatars.githubusercontent.com/u/675644?v=4",
    },
    { 
        "login": "aabadie",
        "avatar_url": "https://avatars.githubusercontent.com/u/1375137?v=4",
    },
    {
        "login": "haukepetersen",
        "avatar_url": "https://avatars.githubusercontent.com/u/620834?v=4",
    },
    {
        "login": "OlegHahm",
        "avatar_url": "https://avatars.githubusercontent.com/u/1590423?v=4",
    },
    {
        "login": "kaspar030",
        "avatar_url": "https://avatars.githubusercontent.com/u/4679640?v=4",
    },
    {
        "login": "benpicco",
        "avatar_url": "https://avatars.githubusercontent.com/u/1301112?v=4",
    },
    {
        "login": "LudwigKnuepfer",
        "avatar_url": "https://avatars.githubusercontent.com/u/3739173?v=4",
    },
    {
        "login": "leandrolanzieri",
        "avatar_url": "https://avatars.githubusercontent.com/u/5381296?v=4",
    },
    {
        "login": "cgundogan",
        "avatar_url": "https://avatars.githubusercontent.com/u/739129?v=4",
    },
    {
        "login": "bergzand",
        "avatar_url": "https://avatars.githubusercontent.com/u/5160052?v=4",
    },
]
DEFAULT_MAINTAINERS = [
    {
        "login": "miri64",
        "avatar_url": "https://avatars.githubusercontent.com/u/675644?v=4",
        "name": "Martine Lenders",
        "html_url": "https://github.com/miri64",
        "admin": True,
        "owner": False,
        "areas": [
            "sys/net",
            "tests/*/tests/*.py",
        ],
    },
    {
        "login": "aabadie",
        "avatar_url": "https://avatars.githubusercontent.com/u/1375137?v=4",
        "name": "Alexandre Abadie",
        "html_url": "https://github.com/aabadie",
        "admin": False,
        "owner": False,
        "areas": [
            "pkg/semtech-loramac/",
            "doc/",
        ],
    },
    {
        "login": "OlegHahm",
        "name": "Oleg Hahm",
        "avatar_url": "https://avatars.githubusercontent.com/u/1590423?v=4",
        "html_url": "https://github.com/OlegHahm",
        "admin": False,
        "owner": True,
        "areas": [],
    },
    {
        "login": "kaspar030",
        "avatar_url": "https://avatars.githubusercontent.com/u/4679640?v=4",
        "name": "Kaspar Schleiser",
        "html_url": "https://github.com/kaspar030",
        "admin": False,
        "owner": True,
        "areas": [
            "sys/include/ztimer.h",
            "pm.c",
        ],
    },
    {
        "login": "benpicco",
        "avatar_url": "https://avatars.githubusercontent.com/u/1301112?v=4",
        "html_url": "https://github.com/benpicco",
        "name": "",
        "admin": True,
        "owner": False,
        "areas": [
            "drivers/at86rf215/",
        ],
    },
    {
        "login": "biboc",
        "avatar_url": "https://avatars.githubusercontent.com/u/4921425?v=4",
        "html_url": "https://github.com/biboc",
        "name": "biboc",
        "admin": False,
        "owner": False,
        "areas": [
            "cpu/samd21/",
        ],
    },
]
DEFAULT_STATS = {
    "boards": len(DEFAULT_BOARDS),
    "cpus": len(DEFAULT_BOARDS),
    "commits": 42
}
