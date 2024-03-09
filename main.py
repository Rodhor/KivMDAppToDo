from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime


class DialogContent(MDBoxLayout):
    # The init function for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y") 

    # This function will show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()
        date_dialog.bind(on_save = self.on_save)

    # This function will get the date and save in a friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)

# This is the main App class
class MainApp(MDApp):
    # Flag
    task_list_dialog = None
    # This is the build function for setting the theme
    def build(self):
        self.theme_cls.primary_palette = ("Teal")
    
    # This is the show task function
    def show_task_function(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title= "Create Task",
                type="custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()
    
    # Adding tasks
    def add_task(self, task, task_date):
        print(f'{task.text} due on {task_date}')

    # This is a dialog closing function
    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    # 

if __name__ == "__main__":
    app = MainApp()
    app.run()
