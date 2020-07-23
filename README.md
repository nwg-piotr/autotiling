# autotiling
This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python)
to switch the layout splith/splitv depending on the currently focused window
dimensions. It works on both sway and i3 window managers.

Inspired by https://github.com/olemartinorg/i3-alternating-layout.

## See on YouTube:

[![Auto-tiling in
action](https://img.youtube.com/vi/UWRZuhn92bQ/0.jpg)](https://www.youtube.com/watch?v=UWRZuhn92bQ)

## Installation

1. Install autotiling. Possible methods:

   * _PyPi._

     [![PyPi
     Version](https://img.shields.io/pypi/v/autotiling.svg?style=flat-square)](https://pypi.org/project/autotiling)

     autotiling is available from PyPi, so you can install it with
     ```
     pip install autotiling
     ```

   * _Arch Linux_

     [![Packaging
     status](https://repology.org/badge/vertical-allrepos/autotiling.svg)](https://repology.org/project/autotiling/versions)

     For the latest development version use
     [autotiling-git](https://aur.archlinux.org/packages/autotiling-git).

   * _Manually_

     1. Install the `python-i3ipc>=2.0.1` package (or whatever it's called in your Linux
        distribution).
     2. Save the `autotiling.py` file anywhere, make executable and autostart in your
        i3/sway config file: `exec /path/to/the/script/autotiling.py` on sway or
        `exec_always --no-startup-id /path/to/the/script/autotiling.py` on i3.

   * _Snap_
     ```
     snap install autotiling
     ```

   _NOTE:_ The current master branch is compatible with sway >= 1.5. For lower versions
   you need to use the script from the [sway14
   branch](https://github.com/nwg-piotr/autotiling/tree/sway14) or the [0.9
   release](https://github.com/nwg-piotr/autotiling/releases/tag/v0.9).


2. Add `exec autotiling` to the `~/.config/sway/config` or `exec_always --no-startup-id
   autotiling` to the `~/.config/i3/config` file.
