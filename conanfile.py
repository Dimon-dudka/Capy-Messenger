from conan import ConanFile

class CapyMessenger(ConanFile):
    name = "CapyMessenger"
    settings = ("os", "compiler", "build_type", "arch")
    generators = ("CMakeDeps", "CMakeToolchain")

    def requirements(self):
        self.requires("nlohmann_json/3.12.0")

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "Third-Party"