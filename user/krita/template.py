pkgname = "krita"
pkgver = "5.2.13"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
	"python",
]
#depends = [

#]
pkgdesc = "Free digital painting application. Digital Painting, Creative Freedom!"
license = "GPL-2.0-or-later"
url = "https://krita.org"
source = f"https://download.kde.org/stable/krita/{pkgver}/krita-{pkgver}.tar.xz"
sha256 = "ddd3955d77a9d760499466c9e7e11a51e080020ee52e929e2579a0aab600b45a"
# Breaks compilation on Musl https://bugs.kde.org/show_bug.cgi?id=412058
options = ["!check"]
