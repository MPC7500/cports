pkgname = "intellij-idea-community"
pkgver = "2025.2.3"
pkgrel = 0

hostmakedepends = [
    "openjdk21-jdk",
]
makedepends = [
    "openjdk21-jdk",
]
depends = [
    "openjdk21-jdk",
]
pkgdesc = "JetBrains IntelliJ IDEA Community Edition"
license = "Apache-2.0"
url = "https://www.jetbrains.com/idea"
source = f"https://download.jetbrains.com/idea/ideaIC-{pkgver}.tar.gz"
sha256 = "6b7c671e97b1419ca22ff4c4a32e7ca51577e4177589bfd321bd9a26df16c9ba"

def build(self):
    pass

def install(self):
    install_dir = "usr/share/intellij-idea-community"
    
    for d in ["bin", "lib", "jbr", "license", "modules", "plugins"]:
        self.cp(d, f"{self.destdir}/{install_dir}/{d}", recursive=True)
    
    self.install_bin(self.files_path / "idea-launcher.sh", name=pkgname)
    self.install_file(self.files_path / "intellij-idea-community.desktop",
                      "usr/share/applications/intellij-idea-community.desktop")
    self.install_file(self.files_path / "idea.png",
                      "usr/share/pixmaps/idea.png")