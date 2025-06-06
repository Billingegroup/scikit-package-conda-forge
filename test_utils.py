#!/usr/bin/env python3
from pathlib import Path

import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
cc_path = (Path.cwd()).resolve()
p = pexpect.spawn(f"cookiecutter {cc_path}")

p.expect("github_username_or_orgname .*")
p.sendline("diffpy")

p.expect("package_import_name .*")
p.sendline("diffpy.my_project")

p.expect("github_repo_name .*")
p.sendline("diffpy.my_project")

p.expect("version .*")
p.sendline("3.4.0")

p.expect("project_short_description .*")
p.sendline("Shared utilities for diffpy packages.")

p.expect("project_full_description .*")
p.sendline(
    "The diffpy.utils package provides functions for extracting array data "
    "from variously formatted text files and wx GUI utilities used by the "
    "PDFgui program. The package also includes an interpolation function "
    "based on the Whittaker-Shannon formula that can be used to resample "
    "a PDF or other profile function over a new grid."
)

p.expect("license_file .*")
p.sendline("LICENSE.txt")

p.expect("recipe_maintainers .*")
p.sendline("sbillinge, bobleesj")

p.expect("build_requirements .*")
p.sendline("")

p.expect("host_requirements .*")
p.sendline("python >=3.10, setuptools, pip")

p.expect("runtime_requirements .*")
p.sendline("python >=3.10, setuptools, numpy >= 1.3")

p.expect("testing_requirements .*")
p.sendline("pytest, pytest-mock, freezegun")

p.expect("test_these_imports .*")
p.sendline("diffpy, diffpy.utils, diffpy.utils.parsers, diffpy.utils.tests")

# Runs until the cookiecutter is done; then exits.
p.interact()
