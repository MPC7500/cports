pkgname = "breeze-icons"
pkgver = "6.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBINARY_ICONS_RESOURCE=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "python-lxml",
]
makedepends = ["qt6-qtbase-devel"]
checkdepends = ["fdupes"]
pkgdesc = "Breeze icon themes"
license = "LGPL-3.0-or-later"
url = "https://api.kde.org/frameworks/breeze-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/breeze-icons-{pkgver}.tar.xz"
sha256 = "946e793b674126db984e2f783be4b348e9c68c2527d34ddd725f9cb0862936b4"
broken_symlinks = [
    # broken symbolic links to 24
    "usr/share/icons/breeze*/animations/24@*x",  # breeze{,-dark}/animations/24@{2,3}x
    "usr/share/icons/breeze/emotes/24@*x",  # 24@{2,3}x
]
hardening = ["vis"]
# over 300 broken symbolic links for size 24 svgs since 6.15..
options = ["brokenlinks"]


@subpackage("breeze-icons-devel")
def _(self):
    return self.default_devel()
