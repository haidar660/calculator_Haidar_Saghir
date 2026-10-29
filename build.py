"""PyBuilder configuration for calculator_Haidar_Saghir."""

from pybuilder.core import Author, init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

name = "calculator_Haidar_Saghir"
version = "1.0.0"
summary = "A calculator project built and tested with PyBuilder"
authors = [Author("Haidar Saghir", "77542825+haidar660@users.noreply.github.com")]
license = "MIT"
default_task = "publish"


@init
def initialize(project):
    """Configure the handout's source and unit-test directories."""
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Haidar_Saghir",
    )
    project.set_property("unittest_module_glob", "test_*")
