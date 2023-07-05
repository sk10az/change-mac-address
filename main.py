import subprocess
import argparse
import string
import random
import re

from simple_term_menu import TerminalMenu


def get_random_mac_address():
    """Generate and return a MAC address in the format of Linux"""
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")


def get_current_mac_address(iface):
    output = subprocess.check_output(f"sudo ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()


def change_mac_address(iface, new_mac_address):
    # disable the network interface
    subprocess.check_output(f"sudo ifconfig {iface} down", shell=True)
    # change the MAC
    subprocess.check_output(f"sudo ifconfig {iface} hw ether {new_mac_address}", shell=True)
    # enable the network interface again
    subprocess.check_output(f"sudo ifconfig {iface} up", shell=True)


def main():
    choose = ['[+] yes', '[-] no']
    menu = TerminalMenu(choose, title='You want change mac-address?', show_shortcut_hints=True)
    menu.show()

    menu_sel = menu.show()
    if menu_sel == 0:
        new_mac_address = 0
        parser = argparse.ArgumentParser(description="Python Mac Changer on Linux")
        parser.add_argument("interface", help="The network interface name on Linux")
        parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
        parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
        args = parser.parse_args()
        iface = args.interface
        if args.random:
            new_mac_address = get_random_mac_address()
        elif args.mac:
            new_mac_address = args.mac
        old_mac_address = get_current_mac_address(iface)
        print("[*] Old MAC address:", old_mac_address)
        change_mac_address(iface, new_mac_address)
        new_mac_address = get_current_mac_address(iface)
        print("[+] New MAC address:", new_mac_address)

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
    elif menu_sel == 1:
        select = ['exit', 'change MAC address']
        menu = TerminalMenu(select, title='Select', show_shortcut_hints=True)
        menu.show()

        menu_sel = menu.show()
        if menu_sel == 0:
            print('Exit')
        elif menu_sel == 1:
            main()


if __name__ == '__main__':
    main()
