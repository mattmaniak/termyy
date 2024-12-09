#! /usr/bin/env python3

import os
import sys

import modules.menu
import modules.controls
import modules.render


def game(mode):
    while True:
        modules.menu.welcome(mode)

        if modules.controls.key_event(modules.state.Screens.PAUSE_MENU):
            round()
        modules.render.flushFrame()


def round():
    while True:
        modules.render.window(modules.render.Player.x, modules.render.Player.y)

        if modules.controls.key_event(modules.state.Screens.GAMEPLAY):
            while True:
                game(modules.state.Screens.PAUSE_MENU)
        modules.render.flushFrame()


if __name__ == "__main__":
    if os.name != "posix":
        sys.stderr.write("Your OS is not supported!\n")
        exit(1)

    game(modules.state.Screens.MAIN_MENU)
else:
    sys.stderr.write("Do not import this file as a module. Run it directly.\n")
