# J0hn_C0nn0r
# Embedded file name: t.py
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, CheckBox, RadioButtons, Button, PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, InvalidFields
import sys
from Crypto.Cipher import AES
import base64
from itertools import cycle, izip
import re
form_data = {'ID': ['CCN-CERT'],
 'RT': ['Robocop'],
 'SN': '1337',
 'Actions': 1}
t = 'VGVybWluYXRvciBUMTAwMA==' # Terminator T1000
key = ''
iv = ''
cs = 'z\xe7\xd5\x1e\xb6sY\x93\xb8V\xfa\xa7~\x11\xce\xba'
s = ''

def new_flash():
    global s
    global key
    global iv
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    s = obj2.decrypt(cs)
    print (s)
    return s


def info_comp(value):
    global key
    x = 'PloreqlarFlfgrzf'	# CyberdyneSystems
    y = x.encode('rot13')
    if value[0] == y.decode('utf-8'):
        key = value[0].encode('ascii', 'ignore')
        return True
    else:
        return False


def info_robot(value):
    global iv
    if value[0] == base64.b64decode(t).decode('utf-8'):
        iv = value[0].encode('ascii', 'ignore')
        return True
    else:
        return False


class DemoFrame(Frame):

    def __init__(self, screen):
        super(DemoFrame, self).__init__(screen, int(screen.height * 3 // 5), int(screen.width * 2 // 3), data=form_data, has_shadow=True, name='My Form')
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        self._validate_button = Button('Search', self._reset)
        layout.add_widget(TextBox(1, label='Company Name:', name='ID', on_change=self._on_change), 1)
        layout.add_widget(TextBox(1, label='Robot Type:', name='RT', on_change=self._on_change), 1)
        layout.add_widget(Text(label='Id Number:', name='SN', on_change=self._on_change, validator='^[0-9]*$'), 1)
        layout.add_widget(Divider(height=2), 1)
        layout.add_widget(RadioButtons([('Go to the past', 1), ('Go to the future', 2), ('Find Sarah', 3)], label='Actions:', name='Actions', on_change=self._on_change), 1)
        layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(self._validate_button, 0)
        self.fix()

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            if key not in form_data or form_data[key] != value:
                changed = True
                break

        self._validate_button.disabled = not changed

    def _reset(self):
        wrong_id = False
        wrong_ro = False
        try:
            message = '[?] Info: \n\n'
            for key, value in self.data.items():
                if key == 'ID':
                    wrong_id = info_comp(value)

            if wrong_id == False:
                message += 'UNKNOWN ID'
            else:
                for key, value in self.data.items():
                    if key == 'RT':
                        wrong_ro = info_robot(value)

                if wrong_ro == True:
                    for key, value in self.data.items():
                        if key == 'Actions':
                            if value == 3:
                                message += new_flash()
                            else:
                                message += 'UNKNOWN ID'

                else:
                    message += 'UNKNOWN ID'
        except InvalidFields as exc:
            message = 'The following fields are invalid:\n\n'
            for field in exc.fields:
                message += '- {}\n'.format(field)

        self._scene.add_effect(PopUpDialog(self._screen, message, ['OK']))


def demo(screen, scene):
    screen.play([Scene([DemoFrame(screen)], -1)], stop_on_resize=True, start_scene=scene)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene