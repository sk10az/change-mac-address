import subprocess
import string
import random
import re

import menu as menu
from simple_term_menu import TerminalMenu


def get_random_address():
    """Generate and return a MAC address in the format of Linux"""
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ''
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)

        mac += ":"

    return mac.strip(":")


def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Edit Menu", "Second Item", "Third Item", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    choose = ['[+] yes', '[-] no']
    menu = TerminalMenu(choose, title='You want change mac-address?', show_shortcut_hints=True)
    menu.show()

    menu_sel = menu.show()
    if menu_sel == 0:
        print(get_random_address())
    elif menu_sel == 1:
        print('ok...')


if __name__ == '__main__':
    main()
