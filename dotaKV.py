import re
import sys
import time

try:
	import thread
except:
	import _thread as thread

import sublime
import sublime_plugin

Pref = {}
settings_base = {}


def Change_Syntax():
	for line open("dotaKV.tmLanguage", "w"):
		

def plugin_loaded():
	global settings_base
	global Pref

	settings = sublime.load_settings('dotaKV.sublime-settings')

	print("HELLO FAGGOT")

	# class Pref:
	# 	def load(self):
	# 		# Pref.color_scope_name                                    = settings.get('color_scope_name', "comment")
	# 		# Pref.highlight_delay                                     = settings.get('highlight_delay', 0)
	# 		# Pref.case_sensitive                                      = (not bool(settings.get('case_sensitive', True))) * sublime.IGNORECASE
	# 		# Pref.draw_outlined                                       = bool(settings.get('draw_outlined', True)) * sublime.DRAW_OUTLINED
	# 		# Pref.mark_occurrences_on_gutter                          = bool(settings.get('mark_occurrences_on_gutter', False))
	# 		# Pref.icon_type_on_gutter                                 = settings.get("icon_type_on_gutter", "dot")
	# 		# Pref.highlight_when_selection_is_empty                   = bool(settings.get('highlight_when_selection_is_empty', False))
	# 		# Pref.highlight_word_under_cursor_when_selection_is_empty = bool(settings.get('highlight_word_under_cursor_when_selection_is_empty', False))
	# 		# Pref.word_separators                                     = settings_base.get('word_separators')
	# 		# Pref.show_status_bar_message                             = bool(settings.get('show_word_highlight_status_bar_message', True))
	# 		# Pref.file_size_limit                                     = int(settings.get('file_size_limit', 4194304))
	# 		# Pref.when_file_size_limit_search_this_num_of_characters  = int(settings.get('when_file_size_limit_search_this_num_of_characters', 20000))
	# 		# Pref.timing                                              = time.time()
	# 		# Pref.enabled                                             = True
	# 		# Pref.prev_selections                                     = None
	# 		# Pref.prev_regions                                        = None
	# 		# Pref.select_next_word_skiped                             = 0
	# 		Pref.

	# Pref = Pref()
	# Pref.load()

	# settings.add_on_change('reload', lambda:Pref.load())
	# settings.add_on_change('reload', lambda:Pref.load())