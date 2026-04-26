"""
Help panel for LichtFeld Studio.
Displays keyboard shortcuts in a two-column table.

Tabs are simulated with styled buttons since ui.tab_bar() is not part
of the immediate-mode draw() API.

Entry format in SHORTCUTS:
    ("HEADING", None, None)             -> section heading row
    (None, "Shortcut", "Description")  -> shortcut entry row
"""

import lichtfeld as lf


SHORTCUTS = [
    # ── GENERAL ─────────────────────────────────────────────────────────────
    ("GENERAL", None, None),
    (None, "Ctrl + Z", "Undo"),
    (None, "Ctrl + Y", "Redo"),

    # ── NAVIGATION ──────────────────────────────────────────────────────────
    ("NAVIGATION", None, None),
    (None, "MMB Drag", "Camera Orbit"),
    (None, "RMB Drag", "Camera Pan"),
    (None, "Scroll", "Camera Zoom"),
    (None, "RMB Double-Click", "Set Pivot"),
    (None, "W", "Move Forward"),
    (None, "S", "Move Backward"),
    (None, "A", "Move Left"),
    (None, "D", "Move Right"),
    (None, "E", "Move Up  \u00b2"),
    (None, "Q", "Move Down  \u00b2"),
    (None, "Ctrl + +", "Increase Move Speed"),
    (None, "Ctrl + -", "Decrease Move Speed"),
    (None, "Ctrl + Shift + +", "Increase Zoom Speed"),
    (None, "Ctrl + Shift + -", "Decrease Zoom Speed"),
    (None, "F", "Focus Camera on Selection"),
    (None, "H", "Go to Home"),
    (None, "\u2192  Right Arrow", "Cycle Camera view \u2013 next image"),
    (None, "\u2190  Left Arrow", "Cycle Camera view \u2013 previous image"),

    # ── TRAINING: IMAGE VIEWER ───────────────────────────────────────────────
    ("TRAINING: IMAGE VIEWER", None, None),
    (None, "\u2190 \u2192", "Navigate"),
    (None, "F", "Fit to window"),
    (None, "1", "Zoom 100%"),
    (None, "+ -  /  Scroll", "Zoom"),
    (None, "I", "Info"),
    (None, "T", "Thumbs"),
    (None, "M", "Mask"),
    (None, "C", "Pick"),
    (None, "R", "Reset"),
    (None, "G", "GT Compare: Split View \u2013 Image (L) & Sparse / 3dGS (R)"),
    (None, "Shift + V", "Toggle Split view (selected 3dGS files)"),
    (None, "Esc", "Close  \u00b9"),

    # ── VIEWER: VIEW CONTROL ─────────────────────────────────────────────────
    ("VIEWER: VIEW CONTROL", None, None),
    (None, "F", "Focus Camera on 3dGS (splat centroid \u2192 Pivot, zoom extents  \u00b3)"),
    (None, "H", "Go to Home (default start view)"),
    (None, "V", "Toggle Compare view (2 vis in tree)"),
    (None, "Shift + V", "Toggle Split view (training of same 3dGS file)"),
    (None, "G", "Toggle Compare view between selected 3dGS files  = V"),

    # ── EDITING \u2013 SELECTION ──────────────────────────────────────────────────
    ("EDITING \u2013 SELECTION", None, None),
    (None, "Ctrl + 1", "Selection: Centers"),
    (None, "Ctrl + 2", "Selection: Rectangle"),
    (None, "Ctrl + 3", "Selection: Polygon"),
    (None, "Ctrl + 4", "Selection: Lasso"),
    (None, "Ctrl + 5", "Selection: Rings"),
    (None, "Ctrl + C", "Copy Selection"),
    (None, "Ctrl + V", "Paste Selection"),
    (None, "Ctrl + I", "Invert Selection"),
    (None, "Ctrl + D", "Deselect All"),
    (None, "LMB Drag", "Selection: Replace"),
    (None, "Shift + LMB Drag", "Selection: Add"),
    (None, "Ctrl + LMB Drag", "Selection: Remove"),
    (None, "X", "Toggle Depth Box"),
    (None, "Ctrl + Alt + C", "Toggle Selection Crop Filter"),
    (None, "Alt + Scroll", "Adjust Depth Box"),

    # ── BRUSH ────────────────────────────────────────────────────────────────
    ("BRUSH", None, None),
    (None, "B", "Cycle Brush Mode  \u00b9"),
    (None, "[ / ]", "Resize Brush"),
    (None, "Shift + LMB Drag", "SAT: increase  /  SEL: Select Add (visible)"),
    (None, "Ctrl + LMB Drag", "SAT: increase  /  SEL: Select Add (hidden until release)  \u00bf"),

    # ── SCENE ────────────────────────────────────────────────────────────────
    ("SCENE", None, None),
    (None, "Delete", "Delete Node in scene"),

    # ── CROP BOX ─────────────────────────────────────────────────────────────
    ("CROP BOX", None, None),
    (None, "Enter", "Apply Crop Box"),
    (None, "Delete", "Apply Crop Box"),
]

FOOTNOTES = (
    "\u00b9 Not working   "
    "\u00b2 Recommended Add (as per SuperSplat)   "
    "\u00b3 Focal length \u224850 mm   "
    "\u00bf Action still to be confirmed"
)

TABS = ["Shortcuts"]


class HelpPanel(lf.ui.Panel):
    """Help & shortcuts reference panel."""

    id = "lfs_help.help_panel"
    label = "Help"
    space = lf.ui.PanelSpace.MAIN_PANEL_TAB
    order = 0

    def __init__(self):
        self._active_tab = 0

    def draw(self, ui) -> None:
        # ── Tab bar (simulated with buttons) ────────────────────────────────
        with ui.row() as row:
            for i, name in enumerate(TABS):
                style = "primary" if i == self._active_tab else "default"
                if row.button_styled(name, style):
                    self._active_tab = i

        ui.separator()

        # ── Tab content ─────────────────────────────────────────────────────
        if self._active_tab == 0:
            self._draw_shortcuts(ui)

    def _draw_shortcuts(self, ui) -> None:
        ui.label("LichtFeld Studio \u2013 Keyboard Shortcuts (v0.5.2)")
        ui.separator()

        for header, shortcut, description in SHORTCUTS:
            if header is not None:
                ui.separator()
                ui.heading(header)
            else:
                with ui.split(0.38) as row:
                    row.label(shortcut)
                    row.label(description)

        ui.separator()
        ui.label(FOOTNOTES)
