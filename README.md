# autotiling
This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout 
splith / splitv depending on the currently focused window dimensions. It works on both sway and i3 window managers.

Inspired by https://github.com/olemartinorg/i3-alternating-layout

## See on YouTube:

[![Auto-tiling in action](https://img.youtube.com/vi/UWRZuhn92bQ/0.jpg)](https://www.youtube.com/watch?v=UWRZuhn92bQ)

## Installation

**Arch Linux**

1. Install the `autotiling` (AUR) package.
2. Add `exec --no-startup-id autotiling` to the `~/.config/sway/config` or to the `~/.config/i3/config` file.


**Manually**

1. Install the `python-i3ipc>=2.0.1` package (or whatever it's called in your Linux distribution).
2. Save the `autotiling.py` file anywhere, make executable and autostart in your i3/sway config file: 
`exec --no-startup-id /path/to/the/script/autotiling.py` on sway or i3.
