# ---------------------------------------------------
# file:     $XDG_CONFIG_HOME/qutebrowser/config.py
# author:   jason ryan ~ yael
# vim:fenc=utf-8:nu:ai:si:et:ts=4:sw=4:ft=python:
# ---------------------------------------------------

# general settings
config.load_autoconfig(False)
#c.url.default_page = 'file:///home/jason/Sync/browser/index.html'
#c.editor.command = ["urxvt", "-title", "scratchpad", "-geometry", "86x24+40+60", "-e", "vim", "-f", "{}"]
c.new_instance_open_target = "tab-bg"
c.input.insert_mode.auto_load = True
c.prompt.filebrowser = False
c.completion.height = "30%"
c.completion.web_history.max_items = 1000
c.input.partial_timeout = 2000
c.tabs.background = True
#c.tabs.favicons.show = "never"
c.tabs.title.format = "{index}.{current_title}"
c.tabs.new_position.related = "last"
c.downloads.location.directory = '/home/yael/downloads/'
c.content.cache.size = 52428800
c.content.webgl = False
c.content.autoplay = False
c.content.geolocation = False
c.content.blocking.enabled = True
c.content.blocking.method = "adblock"
c.content.notifications.enabled = False
c.content.tls.certificate_errors = "ask-block-thirdparty"
c.hints.border = "1px solid #CCCCCC"
c.hints.mode = "number"
c.hints.chars = "123456789"
c.hints.min_chars = 1
c.keyhint.blacklist = ["*"]
c.completion.open_categories = ["quickmarks", "history"]
c.statusbar.widgets = ["url", "progress", "scroll"]
c.zoom.default = "159%"

# searches
c.url.searchengines['DEFAULT'] = 'https://duckduckgo.com/?q={}'
c.url.searchengines['a'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['g'] = 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}'
c.url.searchengines['y'] = 'https://yewtu.be/search?q={}'
c.url.searchengines['w'] = 'https://en.wikipedia.org/w/index.php?search={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}&type=Code'
c.url.searchengines['ap'] = 'https://www.archlinux.org/packages/?sort=&q={}'
c.url.searchengines['ab'] = 'https://bugs.archlinux.org/?project=5&string={}'

# aliases
c.aliases['ge'] = 'open -t https://wiki.archlinux.org/index.php/Forum_Etiquette'
c.aliases['gf'] = 'open -t http://flickr.com/jasonwryan '
c.aliases['gy'] = 'open -t http://anti.moe/~yael/'
c.aliases['gs'] = 'open -t http:/127.0.0.1:8384/'
c.aliases['gr'] = 'open -t https://feedbin.com/'

# colors
c.colors.completion.fg = "#899CA1"
c.colors.completion.category.fg = "#F2F2F2"
c.colors.completion.category.bg = "#555555"
c.colors.completion.item.selected.fg = "white"
c.colors.completion.item.selected.match.fg = "#0080FF"
c.colors.completion.item.selected.bg = "#333333"
c.colors.completion.item.selected.border.top = "#333333"
c.colors.completion.item.selected.border.bottom = "#333333"
c.colors.completion.match.fg = "#66FFFF"
c.colors.statusbar.normal.fg = "#899CA1"
c.colors.statusbar.normal.bg = "#222222"
c.colors.statusbar.insert.fg = "#899CA1"
c.colors.statusbar.insert.bg = "#222222"
c.colors.statusbar.command.bg = "#555555"
c.colors.statusbar.command.fg = "#F0F0F0"
c.colors.statusbar.caret.bg = "#5E468C"
c.colors.statusbar.caret.selection.fg = "white"
c.colors.statusbar.progress.bg = "#333333"
c.colors.statusbar.passthrough.bg = "#4779B3"
c.colors.statusbar.url.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.url.success.http.fg = "#899CA1"
c.colors.statusbar.url.success.https.fg = "#53A6A6"
c.colors.statusbar.url.error.fg = "#8A2F58"
c.colors.statusbar.url.warn.fg = "#914E89"
c.colors.statusbar.url.hover.fg = "#2B7694"
c.colors.tabs.bar.bg = "#222222"
c.colors.tabs.even.fg = "#899CA1"
c.colors.tabs.even.bg = "#222222"
c.colors.tabs.odd.fg = "#899CA1"
c.colors.tabs.odd.bg = "#222222"
c.colors.tabs.selected.even.fg = "white"
c.colors.tabs.selected.even.bg = "#222222"
c.colors.tabs.selected.odd.fg = "white"
c.colors.tabs.selected.odd.bg = "#222222"
c.colors.tabs.indicator.start = "#222222"
c.colors.tabs.indicator.stop = "#222222"
c.colors.tabs.indicator.error = "#8A2F58"
c.colors.hints.bg = "#CCCCCC"
c.colors.hints.match.fg = "#000"
c.colors.downloads.start.fg = "black"
c.colors.downloads.start.bg = "#BFBFBF"
c.colors.downloads.stop.fg = "black"
c.colors.downloads.stop.bg = "#F0F0F0"
c.colors.keyhint.fg = "#FFFFFF"
c.colors.keyhint.suffix.fg = "#FFFF00"
c.colors.keyhint.bg = "rgba(0, 0, 0, 80%)"
c.colors.messages.error.bg = "#8A2F58"
c.colors.messages.error.border = "#8A2F58"
c.colors.messages.warning.bg = "#BF85CC"
c.colors.messages.warning.border = c.colors.messages.warning.bg
c.colors.messages.info.bg = "#333333"
c.colors.prompts.fg = "#333333"
c.colors.prompts.bg = "#DDDDDD"
c.colors.prompts.selected.bg = "#4779B3"

# fonts
c.fonts.default_family = ["tewi", "DejaVu Sans Mono", "Liberation Mono"]
c.fonts.tabs.selected = "17pt tewi"
c.fonts.tabs.unselected = c.fonts.tabs.selected
c.fonts.statusbar = "17pt tewi"
c.fonts.downloads = c.fonts.statusbar 
c.fonts.prompts = c.fonts.statusbar
c.fonts.hints = "19px tewi"
c.fonts.messages.info = "17pt tewi"
c.fonts.keyhint = c.fonts.messages.info
c.fonts.messages.warning = c.fonts.messages.info
c.fonts.messages.error = c.fonts.messages.info
c.fonts.completion.entry = c.fonts.statusbar
c.fonts.completion.category = c.fonts.statusbar

# keybinds
config.unbind('gb', mode='normal')
config.unbind('b', mode='normal')
config.unbind('m', mode='normal')
config.unbind('q', mode='normal')
config.unbind('<Ctrl-B>', mode='normal')
config.bind('<Ctrl-r>', 'restart', mode='normal')
config.bind('<Ctrl-Right>', 'tab-next', mode='normal')
config.bind('<Ctrl-Left>', 'tab-prev', mode='normal')
config.bind('<Ctrl-Shift-Right>', 'tab-move +', mode='normal')
config.bind('<Ctrl-Shift-Left>', 'tab-move -', mode='normal')
config.bind('b', 'back', mode='normal')
config.bind('m', 'forward', mode='normal')
#config.bind('t', 'set-cmd-text -s :open -t', mode='normal')
config.bind('<Ctrl-m>', 'set-cmd-text -s :quickmark-save', mode='normal')
config.bind('<Shift-m>', 'set-cmd-text -s :quickmark-save', mode='normal')
config.bind('<Escape>', 'mode-leave', mode='passthrough')
#config.bind('gi', 'mode-enter insert ;; jseval --quiet var inputs = document.getElementsByTagName("input"); for(var i = 0; i < inputs.length; i++) { var hidden = false; for(var j = 0; j < inputs[i].attributes.length; j++) { hidden = hidden || inputs[i].attributes[j].value.includes("hidden"); }; if(!hidden) { inputs[i].focus(); break; } }')
config.bind('<Ctrl-p>', 'jseval document.location=\'https://pinboard.in/add?next=same&url=\'+encodeURIComponent(location.href)+\'&title=\'+encodeURIComponent(document.title)', mode="normal")
