tox-no-internet
==========================

Workarounds when running `tox` with no internet connection.


## Why

A few issues arise when running `tox` with no internet connection:
* `virtualenv` will reach out to pypi to download the latest version of `pip`, `setuptools`, and `wheel`,
* `pip` will reach out to pypi to download dependencies,
* if your project or one of its dependency uses the `setuptools` *setup_requires* keyword in its *setup.py* script, `easy_install` will be used to fulfill these dependencies and will reach out to pypi as well, (see `pip` documentation on this [topic](https://pip.pypa.io/en/stable/reference/pip_install/#controlling-setup-requires). 


## How it works

First, set the `TOX_PLUGIN_FIND_LINKS` environment variable to the local directoy where your packages are.

Then the plugin will do the following for you:
* set the environment variable `VIRTUALENV_NO_DOWNLOAD`,
* create a `pip.conf` file for each testenv created with *no-index* option set and *find-links* option to point to the local directory you specified in `TOX_PLUGIN_FIND_LINKS`,
* create a `disutils.cfg` file for each testenv created by tox to tell `easy_install` to find packages in the local directory you specified.  


## Installation

```
$ pip install tox-no-internet
# just use tox as you usually would
$ tox ...
```

This tox plugin is inspired by Anthony Sottile's [tox-virtualenv-no-download](https://github.com/asottile/tox-virtualenv-no-download).

