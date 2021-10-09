# -*- coding:utf-8 -*-
from libqtile.config import Group, Key, KeyChord
from libqtile.utils import guess_terminal
from libqtile import bar, layout, widget, hook
from libqtile.lazy import lazy

mod = "mod4"
terminal = guess_terminal('kitty')
browser = "firefox"

def window_to_previous_column_or_group(qtile):
    layout = qtile.current_group.layout
    group_index = qtile.groups.index(qtile.current_group)
    previous_group_name = qtile.current_group.get_previous_group().name

    if layout.name != "columns":
        qtile.current_window.togroup(previous_group_name)
    elif layout.current == 0 and len(layout.cc) == 1:
        if group_index != 0:
            qtile.current_window.togroup(previous_group_name)
    else:
        layout.cmd_shuffle_left()


def window_to_next_column_or_group(qtile):
    layout = qtile.current_group.layout
    group_index = qtile.groups.index(qtile.current_group)
    next_group_name = qtile.current_group.get_next_group().name

    if layout.name != "columns":
        qtile.current_window.togroup(next_group_name)
    elif layout.current + 1 == len(layout.columns) and len(layout.cc) == 1:
        if group_index + 1 != len(qtile.groups):
            qtile.current_window.togroup(next_group_name)
    else:
        layout.cmd_shuffle_right()


def window_to_right_screen(qtile):
    qtile.current_window.toscreen(0)
    qtile.focus_screen(0)

def window_to_left_screen(qtile):
    qtile.current_window.toscreen(1)
    qtile.focus_screen(1)

def switch_screens(qtile):
    if len(qtile.screens) == 1:
        previous_switch = getattr(qtile, "previous_switch", None)
        qtile.previous_switch = qtile.current_group
        return qtile.current_screen.toggle_group(previous_switch)

    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


def get_keybinds():
    keys = [
        # Monitor Switches
        Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
        Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
        Key([mod], "t", lazy.function(switch_screens), desc="Switch to another screen"),

        Key([mod, "shift"], "Left", lazy.function(window_to_left_screen)),
        Key([mod, "shift"], "Right", lazy.function(window_to_right_screen)),

        # Switch between windows
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        # Move windows between left/right columns or move up/down in current stack.R
        # Moving out of range in Columns layout will create new column.
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
        Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left",
        ),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.spawn("rofi -show combi"),
            desc="Combination of all methods"
        ),
        Key([mod, "shift"], "p", lazy.spawn("rofi-pass"), desc="Passwords"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),

        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

        Key(
            [mod],
            "r",
            lazy.spawn("rofi -show drun"),
            desc="Spawn a command using a prompt widget",
        ),
        KeyChord(
            [mod],
            "c",
            [
                Key(
                    [],
                    "n",
                    lazy.spawn("code --new-window"),
                    desc="Launch a new session of VS Code instead of restoring the previous session (default).",
                ),
                Key(
                    [],
                    "r",
                    lazy.spawn("code --reuse-window"),
                    desc="Forces opening a file or folder in the last active window.",
                ),
                Key(
                    [],
                    "c",
                    lazy.spawn("code"),
                    desc="Launch VS Code with default definitions",
                ),
            ],
        ),
        ## Treetab controls
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.move_left(),
            desc="Move up a section in treetab",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.move_right(),
            desc="Move down a section in treetab",
        ),
        
        # Change the volume if our keyboard has keys
        Key(
            [], "XF86AudioRaiseVolume",
            lazy.spawn("amixer -c 1 -q set Master 2dB+")
        ),
        Key(
            [], "XF86AudioLowerVolume",
            lazy.spawn("amixer -c 1 -q set Master 2dB-")
        ),
        Key(
            [], "XF86AudioMute",
            lazy.spawn("amixer -D pulse set Master toggle")
        ),
    ]

        # Idea taken from Augusto Nicola's Dotfiles => https://github.com/AugustoNicola/dotfiles
    group_names = [
        ("SYS", {"label": "ﬦ", "layout": "columns"}),
        ("VER", {"label": "", "layout": "columns"}),
        ("WWW", {"label": "", "layout": "columns"}),
        ("DIS", {"label": "ﭮ", "layout": "columns"}),
        ("TEAMS", {"label": "", "layout": "columns"}),
        ("DOC", {"label": "", "layout": "columns"}),
        ("MUS", {"label": "", "layout": "columns"}),
        ("VID", {"label": "嗢", "layout": "columns"}),
        ("VBOX", {"label": "", "layout": "columns"}),
    ]

    groups = [
        Group(name, init=True, persist=True, **kwargs) for name, kwargs in group_names
    ]

    for i, (name, kwargs) in enumerate(group_names, 1):
        keys.append(
            Key([mod], str(i), lazy.group[name].toscreen())
        )  # Switch to another group
        keys.append(
            Key([mod, "shift"], str(i), lazy.window.togroup(name))
        )  # Send current window to another group

    return keys, groups



# groups = [Group(i) for i in "123456789"]
# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])


# if __name__ == "__main__":
#     print(get_keys())
