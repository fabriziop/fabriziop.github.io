#!/usr/bin/python
# .+
#
# .identifier :	$Id:$
# .context    : Application View Controller
# .title      : A table of all supported widget/control type conbinations (GTK3)
# .kind	      : python source
# .author     : Fabrizio Pollastri
# .site	      : Revello - Italy
# .creation   :	20-Mar-2015
# .copyright  : (c) 2015 Fabrizio Pollastri.
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


import gi.repository.GObject as GObject	#--
import gi.repository.Gtk as Gtk		#- gimp tool kit bindings

from avc import *			# AVC

UI_XML = 'gtk3_showcase.ui'		# GUI descriptor
ROOT_WINDOW = 'root_window'		# root window name
INCREMENTER_PERIOD = 333		# ms


class Example(AVC):
  """
  A table of all supported widget/control type combinations
  """

  def __init__(self):

    # create GUI
    self.builder = Gtk.Builder()
    self.builder.add_from_file(UI_XML)
    self.builder.connect_signals(self)
    self.root_window = self.builder.get_object(ROOT_WINDOW)
    self.root_window.show_all()

    # the control variables
    self.boolean1 = False
    self.boolean2 = False
    self.radio = 0
    self.integer = 0
    self.float = 0.0
    self.progressbar = -1.0
    self.string = ''
    self.textview = ''
    self.status = ''

    # start variables incrementer
    increment = self.incrementer()
    GObject.timeout_add(INCREMENTER_PERIOD,increment.next) 


  def incrementer(self):
    """
    Booleans are toggled, radio button index is rotated from first to last,
    integer is incremented by 1, float by 0.5, progress bar is alternatively
    shuttled or incremented from 0 to 100%, string is appended a char
    until maxlen when string is cleared, text view/edit is appended a line
    of text until maxlen when it is cleared. Status bar message is toggled.
    Return True to keep timer alive.
    """
    while True:

      self.boolean1 = not self.boolean1
      yield True

      self.boolean2 = not self.boolean2
      yield True

      if self.radio >= 2:
        self.radio = 0
      else:
        self.radio += 1
      yield True

      self.integer += 1
      yield True

      self.float += 0.5
      yield True

      if self.progressbar >= 0.9999:
        self.progressbar = -1.0
      else:
        self.progressbar += 0.1
      yield True

      if len(self.string) >= 10:
        self.string = ''
      else:
        self.string += 'A'
      yield True

      if len(self.textview) >= 200:
        self.textview = ''
      else:
        self.textview += 'line of text, line of text, line of text\n'
      yield True

      if not self.status:
        self.status = 'status message'
      else:
        self.status = ''
      yield True


  def on_destroy(self,window):
    "Terminate program at window destroy"
    Gtk.main_quit()


#### MAIN

example = Example()			# instantiate the application
example.avc_init()			# connect widgets with variables
Gtk.main()			 	# run GTK event loop until quit

#### END
