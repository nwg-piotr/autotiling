#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
This script uses the i3ipc python module to switch the layout splith / splitv
for the currently focused window, depending on its dimensions.
It works on both sway and i3 window managers.

Inspired by https://github.com/olemartinorg/i3-alternating-layout

Copyright: 2019-2020 Piotr Miller & Contributors
e-mail: nwg.piotr@gmail.com
Project: https://github.com/nwg-piotr/autotiling
License: GPL3

Dependencies: python-i3ipc>=2.0.1 (i3ipc-python)
"""
import argparse
import sys
from functools import partial

from i3ipc import Connection, Event


def switch_splitting(i3, e, debug):
    try:
        con = i3.get_tree().find_focused()
        if con:
            if con.floating:                         # We're on i3: on sway it would be None
                is_floating = '_on' in con.floating  # May be 'auto_on' or 'user_on'
                is_full_screen = con.fullscreen_mode == 1
            else:                                    # We are on sway
                is_floating = con.type == 'floating_con'
                # On sway on 1st focus the parent container returns 1, then forever the focused container itself
                is_full_screen = con.fullscreen_mode == 1 or con.parent.fullscreen_mode == 1

            is_stacked = con.parent.layout == 'stacked'
            is_tabbed = con.parent.layout == 'tabbed'

            # Let's exclude floating containers, stacked layouts, tabbed layouts and full screen mode
            if not is_floating and not is_stacked and not is_tabbed and not is_full_screen:
                new_layout = 'splitv' if con.rect.height > con.rect.width else 'splith'
                if new_layout != con.parent.layout:
                    result = i3.command(new_layout)
                    if result[0].success and debug:
                        print('Debug: Switched to {}'.format(new_layout), file=sys.stderr)
                    elif debug:
                        print('Error: Switch failed with err {}'.format(result[0].error), file=sys.stderr)

        elif debug:
            print('Debug: No focused container found', file=sys.stderr)

    except Exception as e:
        print('Error: {}'.format(e), file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Print debug messages to stderr'
    )
    args = parser.parse_args()
    handler = partial(switch_splitting, debug=args.debug)
    i3 = Connection()
    i3.on(Event.WINDOW_FOCUS, handler)
    i3.main()


if __name__ == "__main__":
    main()
