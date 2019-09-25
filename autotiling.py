#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
This script uses the i3ipc python module to switch the layout splith / splitv
for the currently focused window, depending on its dimensions.
It works on both sway and i3 window managers.

Inspired by https://github.com/olemartinorg/i3-alternating-layout

Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
Project: https://github.com/nwg-piotr/autotiling
License: GPL3

Dependencies: python-i3ipc>=2.0.1 (i3ipc-python)
"""

from i3ipc import Connection, Event

i3 = Connection()


def switch_splitting(i3, e):
    try:
        con = i3.get_tree().find_focused()
        if con.floating:                         # We're on i3: on sway it would be None
            is_floating = '_on' in con.floating  # May be 'auto_on' or 'user_on'
            is_full_screen = con.fullscreen_mode == 1
        else:                                    # We are on sway
            is_floating = con.type == 'floating_con'
            # On sway on 1st focus the parent container returns 1, then forever the focused container itself
            is_full_screen = con.fullscreen_mode == 1 or con.parent.fullscreen_mode == 1

        is_tabbed = con.parent.layout == 'tabbed'

        # Let's exclude floating containers, tabbed layouts and full screen mode
        if not is_floating and not is_tabbed and not is_full_screen:
            new_layout = 'splitv' if con.rect.height > con.rect.width else 'splith'
            i3.command(new_layout)

    except Exception as e:
        print('Error: {}'.format(e))
        pass


def main():
    i3.on(Event.WINDOW_FOCUS, switch_splitting)
    i3.main()


if __name__ == "__main__":
    main()
