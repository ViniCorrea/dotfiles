# -*- coding:utf-8 -*-

import os
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen

colors = [
    ["#1d1f21", "#1d1f21"],  # panel background
    ["#1d1f21", "#1d1f21"],  # background for current screen tab
    ["#ecf0ed", "#ecf0ed"],  # font color for group names
    ["#c4c8c5", "#c4c8c5"],  # border line color for current tab
    [
        "#80a1bd",
        "#80a1bd",
    ],  # border line color for 'other tabs'
    ["#80a1bd", "#80a1bd"],  # color for the 'even widgets'
    ["#9BC3BC", "#9BC3BC"],  # window name
    ["#545B68", "#545B68"],  # background for inactive screens
]

def widget_left():
    return [
        widget.CurrentLayoutIcon(
            foreground=colors[0],
            background=colors[1],
            padding=0,
            scale=0.7,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0],
        ),
    ]

def widget_rigth():
    return [
        widget.Systray(icon_size=16, background=colors[0], padding=5),
        widget.Spacer(10),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch",
            display_format="{updates} Updates",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    "kitty -e sudo yay -Syu"
                )
            },
            foreground=colors[3],
        ),
        widget.Spacer(10),
        widget.Clipboard(),
        # Volume
        widget.TextBox(
            text="墳", foreground=colors[3], padding=6, fontsize=23
        ),
        widget.Volume(foreground=colors[3]),
        widget.Spacer(10),
        # CPU
        widget.TextBox(
            text="", fontsize=23, padding=8, foreground=colors[3]
        ),
        widget.CPU(format="{load_percent}%", foreground=colors[3]),
        widget.Spacer(10),
        # Memory
        widget.TextBox(text='', fontsize=20, foreground=colors[3]),
        widget.MemoryGraph(
            line_width=2,
            border_width=1,
            samples=60,
            ),
        widget.Spacer(10),
        # Time
        widget.TextBox(
            text="", fontsize=21, padding=6, foreground=colors[3]
        ),
        widget.Clock(foreground=colors[3], format="%d-%m-%Y | %a %H:%M"),
        widget.Spacer(10),
    ]

def widgets_group_box():
    groupbox_defaults = dict(
        margin_y=3,
        margin_x=0,
        padding_y=7,
        padding_x=7,
        borderwidth=3,
        active=colors[2],
        inactive=colors[7],
        rounded=False,
        highlight_color=colors[1],
        highlight_method="line",
        this_current_screen_border=colors[6],
        this_screen_border=colors[4],
        other_current_screen_border=colors[6],
        other_screen_border=colors[4],
        foreground=colors[2],
        background=colors[0],
    )
    return [
        widget.Sep( # Separator
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0],
        ),
        widget.GroupBox(
            visible_groups=["SYS"],
            font="FiraCode Nerd Font",  # ? using the font is vital for loading the icon
            fontsize=15,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["DEV"],
            font="FiraCode Nerd Font",
            fontsize=17,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["WWW"],
            font="Font Awesome 5 Free",
            fontsize=25,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["DIS"],
            font="FiraCode Nerd Font",
            fontsize=16,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["TEAMS"],
            font="FiraCode Nerd Font",
            fontsize=17,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["DOC"],
            font="Font Awesome 5 Free",
            fontsize=20,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["MUS"],
            font="Font Awesome 5 Free",
            fontsize=27,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["VID"],
            font="Font Awesome 5 Free",
            fontsize=20,
            **groupbox_defaults
        ),
        widget.GroupBox(
            visible_groups=["VBOX"],
            font="Font Awesome 5 Free",
            fontsize=20,
            **groupbox_defaults
        ),
        widget.Spacer(10),
    ]

def widgets_center():
    return [
        # WindowName
        widget.WindowName(
            format="﫳 {name}",
            max_chars=80,
            background=colors[0],
            foreground=colors[6],
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#0000ff", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
    ]

# http://docs.qtile.org/en/latest/manual/ref/widgets.html
def get_two_screens():
    screens = [
        Screen(
            bottom=bar.Bar(
                widget_left() + widgets_group_box() + widgets_center() + widget_rigth(),
                24,
                background=colors[0],
            ),
        ),
        Screen(
            bottom=bar.Bar(
                widget_left() + widgets_group_box() + widgets_center() + widget_rigth(),
                24,
                background=colors[0],
            ),
        ),
    ]

    return screens
