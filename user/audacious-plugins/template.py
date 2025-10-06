pkgname = "audacious-plugins"
pkgver = "4.5.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dqt=false",
    "-Dgtk=true"
]
hostmakedepends = [
	"gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "audacious-devel",
    "curl-devel",
    "faad2-devel",
    "ffmpeg-devel",
    "flac-devel",
    "fluidsynth-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libbs2b-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libcue-devel",
    "libmms-devel",
    "libmodplug-devel",
    "libogg-devel",
    "libsamplerate-devel",
    "libvorbis-devel",
    "mpg123-devel",
    "neon-devel",
    "openssl3-devel",
    "opusfile-devel",
    "soxr-devel",
    "wavpack-devel",
]
depends = [
    "audacious",
]
pkgdesc = "Plugins für den Audacious Audio-Player"
license = "BSD-2-Clause"
url = "https://audacious-media-player.org"
source = f"https://distfiles.audacious-media-player.org/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f4feedc32776acfa9d24701d3b794fc97822f76da6991e91e627e70e561fdd3b"

def post_install(self):
    self.install_license("COPYING")