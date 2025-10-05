pkgname = "audacious-plugins"
pkgver = "4.5.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "audacious-devel",
    "ffmpeg-devel",
    "fluidsynth-devel",
    "glib-devel",
    "libogg-devel",
    "libsamplerate-devel",
    "libvorbis-devel",
    "pipewire-devel",
    "pulseaudio-qt-devel",
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
    
@subpackage("audacious-plugins-devel")
def _(self):
    return self.default_devel()