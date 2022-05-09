#!/usr/bin/env jython
# .+
# .context    : Application View Controller
# .title      : A radio button replicated into a label (Swing),
#		GUI programmatically generated
# .kind	      : python source
# .author     : Fabrizio Pollastri
# .site	      : Torino - Italy
# .creation   :	22-Oct-2009
# .copyright  : (c) 2009 Fabrizio Pollastri.
# .license    : GNU General Public License (see below)
#
# This file is part of "AVC, Application View Controller".
#
# AVC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# AVC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# .-

from javax import swing			# swing toolkit bindings
from java import awt			# awt toolkit bindings

from avc import *			# AVC for Swing


class Example(AVC):
  """
  A radio button whose value is replicated into a label
  """

  def __init__(self):

    # create GUI
    root = swing.JFrame('AVC Swing radio button example',size=(350,100),
      defaultCloseOperation = swing.JFrame.EXIT_ON_CLOSE)
    root.layout = awt.FlowLayout()
    root.add(swing.JLabel('index',name='radio__label',))
    radio_button1 = swing.JRadioButton('choice 0',name='radio__radiobutton1')
    radio_button2 = swing.JRadioButton('choice 1',name='radio__radiobutton2')
    radio_button3 = swing.JRadioButton('choice 2',name='radio__radiobutton3')
    radio_group = swing.ButtonGroup()
    radio_group.add(radio_button1)
    radio_group.add(radio_button2)
    radio_group.add(radio_button3)
    radio_box = swing.Box(swing.BoxLayout.Y_AXIS)
    radio_box.add(radio_button1)
    radio_box.add(radio_button2)
    radio_box.add(radio_button3)
    root.add(radio_box)
    root.show()

    # the variable holding the radio button selection index
    self.radio = 0


#### MAIN

example = Example()			# instantiate the application
example.avc_init()			# connect widgets with variables

#### END
