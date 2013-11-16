import sublime
import sublime_plugin


class AutoWidth(object):
    def __init__(self):
        super(AutoWidth, self).__init__()

    def plugin_loaded_setup(self):
        settings_file = 'AutoWidth.sublime-settings'
        self.settings = sublime.load_settings(settings_file)

    def enabled(self, view):
        if view.settings().get('auto_width'):
            return True

    def get_viewport_chars(self, view):
        return view.viewport_extent()[0] / view.em_width()

    def get_layout_chars(self, view):
        return view.layout_extent()[0] / view.em_width()

    def get_linenumbers_chars(self, view):
        if view.settings().get('line_numbers'):
            lines = view.rowcol(view.size())[0] + 1
            return len(str(lines))
        else:
            return 0

    def update_view(self, view):
        threshold = 4
        adjustment = 2
        layout_chars = self.get_layout_chars(view)
        viewport_chars = self.get_viewport_chars(view)
        if layout_chars > viewport_chars:
            if (self.settings.get('reduce_font_size') and not
                    view.settings().get('font_size_override')):
                new_font_size = (view.settings().get('font_size')
                                 - self.settings.get('font_size_reduction'))
                view.settings().set('font_size', new_font_size)
                view.settings().set('font_size_override', 1)
                # Recalculate char widths
                layout_chars = self.get_layout_chars(view)
                viewport_chars = self.get_viewport_chars(view)
            linenumbers_chars = self.get_linenumbers_chars(view)
            view.settings().set('wrap_width',
                                viewport_chars - linenumbers_chars
                                - adjustment)
        elif layout_chars < viewport_chars - threshold - adjustment:
            for s in ['wrap_width', 'font_size', 'font_size_override']:
                view.settings().erase(s)
            view.settings().set('wrap_width',
                                view.settings().get('wrap_width'))

    def run_once(self, view):
        if self.enabled(view):
            self.update_view(view)


class AutoWidthCommand(sublime_plugin.ApplicationCommand):
    def run(self, **args):
        view = sublime.active_window().active_view()
        auto_width.run_once(view)


class AutoWidthListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        auto_width.run_once(view)

    def on_load(self, view):
        auto_width.run_once(view)


auto_width = AutoWidth()


def plugin_loaded():
    auto_width.plugin_loaded_setup()
