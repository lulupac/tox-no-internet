from __future__ import absolute_import, print_function, unicode_literals

import os
import contextlib
import glob

import tox.venv
from tox import hookimpl


VENV_NO_DOWNLOAD = 'VIRTUALENV_NO_DOWNLOAD'


PIP_CONF_FILE = """
[install]
no-cache-dir = false
no-index = true
find-links = {0}
"""


DISTUTILS_CFG_FILE = """
[easy_install]
allow_hosts = ''
find_links = {0}
"""


@contextlib.contextmanager
def _set_plugin_environ():
    orig = os.environ.get(VENV_NO_DOWNLOAD)
    os.environ[VENV_NO_DOWNLOAD] = '1'
    try:
        yield
    finally:
        if orig is not None:
            os.environ[VENV_NO_DOWNLOAD] = orig
        else:
            os.environ.pop(VENV_NO_DOWNLOAD, None)


@hookimpl(tryfirst=True)
def tox_testenv_create(venv, action):

    with _set_plugin_environ():
        tox.venv.tox_testenv_create(venv, action)

    find_links_url = os.environ.get('TOX_PLUGIN_FIND_LINKS')

    # create pip.conf file in test virtualenv
    pip_conf_path = os.path.join(str(venv.path), "pip.conf")
    with open(pip_conf_path, "w") as fd:
        fd.write(PIP_CONF_FILE.format(find_links_url))

    # create distutils.cfg file in test virtualenv
    path_pattern = os.path.join(str(venv.path), "lib/python*/distutils/distutils.cfg")
    distutils_cfg_path = glob.glob(path_pattern).pop()
    with open(distutils_cfg_path, "w") as fd:
        fd.write(DISTUTILS_CFG_FILE.format(find_links_url))

    # return non-None to indicate we handled the virtualenv creation
    return True
