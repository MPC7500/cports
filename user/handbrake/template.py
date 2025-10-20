pkgname = "handbrake"
pkgver = "1.10.2"
pkgrel = 0
build_style = "configure"
configure_script = "configure"
configure_args = [
    "--enable-gtk",
    "--prefix=/usr",
]
make_dir = "build"
hostmakedepends = [
	"autoconf",
	"automake",
	"cmake",
    "gmake",
    "meson",
    "nasm",
    "pkgconf",
    "python",
]
makedepends = [
    "bzip2-devel",
    "jansson-devel",
    "libass-devel",
    "libbluray-devel",
    "libdvdnav-devel",
    "libdvdread-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libogg-devel",
    "libsamplerate-devel",
    "libtheora-devel",
    "libtool",
    "libvorbis-devel",
    "libvpx-devel",
    "numactl-devel",
    "x264-devel",
    "x265-devel",
    "zlib-ng-devel",
]
depends = [
    "gtk+3",
]
pkgdesc = "Open-source video transcoder with GTK GUI"
license = "GPL-2.0-only"
url = "https://handbrake.fr"
source = f"https://github.com/HandBrake/HandBrake/releases/download/{pkgver}/HandBrake-{pkgver}-source.tar.bz2"
sha256 = "c65e1cc4f8cfc36c24107b92c28d60e71ef185ec983e9a5841facffafea5f8db"
# no good tests
options = ["!check"]

def configure(self):
    self.mkdir("build")
    self.do("../configure", *self.configure_args, wrksrc="build")