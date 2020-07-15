# autotiling
This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout 
splith / splitv depending on the currently focused window dimensions. It works on both sway and i3 window managers.

Inspired by https://github.com/olemartinorg/i3-alternating-layout

## See on YouTube:

[![Auto-tiling in action](https://img.youtube.com/vi/UWRZuhn92bQ/0.jpg)](https://www.youtube.com/watch?v=UWRZuhn92bQ)

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/autotiling.svg)](https://repology.org/project/autotiling/versions)

**Arch Linux**

1. Install the `autotiling` (AUR) package.
2. Add `exec autotiling` to the `~/.config/sway/config` or `exec_always --no-startup-id autotiling` 
to the `~/.config/i3/config` file.

For use with the sway-git package use [autotiling-git](https://aur.archlinux.org/packages/autotiling-git).


**Manually**

NOTE: Current master branch is only compatible with the development (not yet released) version of sway.
For sway version <= 1.4 you need to use the script from the [sway14 branch](https://github.com/nwg-piotr/autotiling/tree/sway14).

1. Install the `python-i3ipc>=2.0.1` package (or whatever it's called in your Linux distribution).
2. Save the `autotiling.py` file anywhere, make executable and autostart in your i3/sway config file: 
`exec /path/to/the/script/autotiling.py` on sway or `exec_always --no-startup-id /path/to/the/script/autotiling.py` on i3.

**Snap**

`snap install autotiling`
