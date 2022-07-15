# PyComArch: py-compress-archive

![](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&style=plastic)
![](https://img.shields.io/badge/-Windows-0078D6.svg?logo=windows&style=flat) ![](https://img.shields.io/badge/-PowerShell-3776AB.svg?logo=PowerShell&style=plastic)

A CLI tool to compress archives with useful features.

In windows, there is no rich zip command, though Compress-Archive exists.
But Linux has.

The goal of this project is providing a rich `Compress-Archive` command.
(`Compress-Archive` is a command on PowerShell, which provides a simple function to compress archives.)
Hence this documentation is based on Windows and PowerShell :)

## features

- compress archives
  - support recursively compress.
- exclude by glob patterns
  - `Compress-Archive` can't exclude. Or it needs to be a hassle.

## usage

### 1. install

```
pip install https://github.com/Take-Me1010/PyComArch.git
```

Or you can download pycomarch folder and using is by setting an alias for `cli.py`.

### 2. call

```
C:\Users\take-me1010> pycomarch -h
usage: pycomarch [-h] [--include-patterns [INCLUDE_PATTERNS ...]] [-x [EXCLUDE_PATTERNS ...]] [-r] [-v] dest src

A CLI tool to compress archives with useful features.

positional arguments:
  dest                  a destination file name
  src                   a src file or directory to zip

options:
  -h, --help            show this help message and exit
  --include-patterns [INCLUDE_PATTERNS ...]
                        a list of patterns to include files or directories even if it matches exclude_patterns. You can use     
                        any rule supported by glob.
  -x [EXCLUDE_PATTERNS ...], --exclude-patterns [EXCLUDE_PATTERNS ...]
                        a list of patterns to ignore files or directories. You can use any rule supported by glob.
  -r, --recursive       determine if zip directory recursively.
  -v, --verbose
```

### 3. set alias (optional)

- Open your profile by `code $PROFILE` or some other way like `vim $PROFILE`.
- Add the following code in the bottom of the your profile.

```$PROFILE
function zip() {
    pycomarch $args
}
```

You can use pycomarch like the following style if you set the alias.

```
C:\Users\take-me1010> zip -h
... (same as the output obtained by using `pycomarch -h`)
```
