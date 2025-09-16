pkgname = "shortwave"
pkgver = "5.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--prefix=/usr",
#    "--buildtype=release",
#    "-Dwrap_mode=nodownload",
]

hostmakedepends = [
    "cargo",
    "desktop-file-utils",
    "gettext",
    "git",
    "libxml2-progs",
    "meson",
    "pkgconf",
]

makedepends = [
#	"cairo-devel",
    "dbus-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "lcms2-devel",
    "libadwaita-devel",
    "libseccomp-devel",
    "libshumate-devel",
    "openssl3-devel",
    "sqlite-devel",
]

pkgdesc = "Listen to internet radio"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Shortwave"
source = [
    f"{url}/-/archive/{pkgver}/Shortwave-{pkgver}.tar.gz",
#    f"file://Shortwave-{pkgver}-vendor.tar.gz",
]

sha256 = [
    "982f74b7a75f592929dbca200bc7d9260f8937e69b7e41fb5b5c360b39c7a13e",
#    "236c782c4a830af2e329e7e939db3487d1eb427c4f1777095db649ead089a5e3",  
]

# No testsuite available
options = ["!check"]

#def configure(self):
#    self.do(
#        "meson", "setup",
#        self.chroot_cwd,# / f"shortwave-{self.pkgver}",
#        "build",
#        "--prefix=/usr"
#    )

def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)