pkgname = "gnugo"
pkgver = "3.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = []
configure_gen = []

pkgdesc = "Free program that plays the game Go"
license = "GPL-2.0-or-later"
url = "https://www.gnu.org/software/gnugo"
source = f"$(GNU_SITE)/gnugo/gnugo-{pkgver}.tar.gz"
sha256 = "da68d7a65f44dcf6ce6e4e630b6f6dd9897249d34425920bfdd4e07ff1866a72"
tool_flags = {"CFLAGS": ["-fcommon"]}