import dearpygui.dearpygui as dpg
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from imagechopper import imagechop

#Tk().withdraw()
dpg.create_context()

def save_path():
    dpg.set_item_user_data(openfilebutton, askopenfilename())

def image_chop_helper():
    imagechop(dpg.get_item_user_data(openfilebutton), dpg.get_value(dropdown))

# main window
with dpg.window(tag="Primary"):
    
    openfilebutton = dpg.add_button(tag=1, label="Select image", width=120, height=30, pos=(90, 40))
    dpg.set_item_callback(openfilebutton, save_path)

    dpg.add_text("Number of chops", pos=(97,85))
    dropdown = dpg.add_combo(tag=2, items=(4, 9, 16), default_value="4", width=70, pos=(115, 110))

    chopbutton = dpg.add_button(tag=3, label="Chop", width=120, height=40, pos=(90, 150))
    dpg.set_item_callback(chopbutton, image_chop_helper)


#dpg.show_item_registry()
#dpg.show_style_editor()

with dpg.theme() as global_theme:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (160, 150, 135))
dpg.bind_theme(global_theme)

dpg.create_viewport(title='Image Splitter', width=300, height=260, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary", True)
dpg.start_dearpygui()
dpg.destroy_context()