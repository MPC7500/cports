pkgname = "mtr"
pkgver = "0.95"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "libtool",
    "m4",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "jansson-devel",
    "libcap-devel",
    "libpcap-devel",
    "ncurses-devel",
    "pkgconf"
]
depends = [
    "jansson",
    "libcap",
    "libpcap",
    "ncurses-libs",
]
# Optionally skip check by default; enable if you want to run tests in CI
#options = ["!check"]

pkgdesc = "Combines the functionality of traceroute and ping into one tool"
license = "GPL-2.0-only"
url = "https://www.bitwizard.nl/mtr/"
source = f"https://www.bitwizard.nl/mtr/files/mtr-{pkgver}.tar.gz"
sha256 = "SKIP"