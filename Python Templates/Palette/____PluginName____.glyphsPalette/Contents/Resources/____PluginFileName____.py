# encoding: utf-8

from plugin import *
from AppKit import *
from GlyphsApp import *


class ____PluginClassName____ (PalettePlugin):
	
	dialog = objc.IBOutlet()
	textField = objc.IBOutlet()
	
	def settings(self):
		self.name = 'My Palette'
		self.dialogName = '____PaletteView____'
	
	def start(self):

		# Adding a callback for the 'GSUpdateInterface' event
		s = objc.selector( self.update, signature="v@:" )
		NSNotificationCenter.defaultCenter().addObserver_selector_name_object_( self, s, "GSUpdateInterface", None )

	def update( self, sender ):

		text = []

		# Extract font from sender
		font = sender.object()

		# We’re in the Edit View
		if font.currentTab:
			# Check whether glyph is being edited
			if len(font.selectedLayers) == 1:
				layer = font.selectedLayers[0]
				text.append('Selected nodes: %s' % len(layer.selection))
				if layer.selection:
					text.append('Selection bounds: %sx%s' % (int(layer.selectionBounds.size.width), int(layer.selectionBounds.size.height)))

		# We’re in the Font view
		else:
			text.append('Selected glyphs: %s' % len(font.selection))

		# Send text to dialog to display
		self.textField.setStringValue_('\n'.join(text))
			
	def quit(self):
		
		# Unload callback
		NSNotificationCenter.defaultCenter().removeObserver_(self)