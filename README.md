# AutoWidth

A Sublime Text plugin to automatically adjust the text wrap width when the view becomes narrower than the pre-defined wrap width.

If you set a fixed `wrap_width` in the syntax specific settings for editing text (e.g. Markdown, reStructuredText), but sometimes have a window that's narrower than this `wrap_width` (for example when using several panes next to each other), this plugin will dynamically adjust the `wrap_width` to fit the view.

By default, the font size is also reduced by 1 when reducing wrap width. This behavior can be adjusted in the AutoWidth settings file, accessible in the Sublime Text preferences menu.

## Installation

Tested on Sublime Text 3 only.

Via [Package Control](https://sublime.wbond.net/).

## Use

Set `"auto_width": true` either in your global settings, or, more usefully, in syntax-specific settings. For example, consider these syntax-specific settings for Markdown:

```json
{
    "draw_centered": true,
    "font_size": 14,
    "line_numbers": false,
    "wrap_width": 98,
    "auto_width": true
}
```

These settings will display Markdown text in a 98 character wide and centered column, without line numbers, and in a larger font.

With `auto_width` enabled, Sublime Text will also automatically adjust the wrap width downwards if necessary if the view becomes too narrow, and then reset it to its default specified in the settings file when the view is wide enough again.

Wrap width is adjusted whenever a view becomes active. If you resize a window you can force an adjust by pressing `F10` (`FN+F10` on OS X).

## License

[GNU GPL version 3](https://www.gnu.org/licenses/gpl.html)
