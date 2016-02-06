name = "cmake"

version = "3.4.3"

description = \
    """
    CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner
    """

variants = [
    ["platform-linux"]
]

uuid = "repository.cmake"

def commands():
    env.PATH.prepend("{root}/bin")
    #env.CMAKE_MODULE_PATH.append("{root}/cmake")
    #env.LD_LIBRARY_PATH.append("{root}/lib")
