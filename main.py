from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (300, 500)

SAKURA = get_color_from_hex("#CCA0A0")
PINK = get_color_from_hex("#CF7381")
SEQUOIA = get_color_from_hex("#795654")
SCARLET = get_color_from_hex("#A3334B")
VINO = get_color_from_hex("#531C24")

Window.clearcolor = VINO

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(orientation="vertical", **kwargs)

        # APP
        self.result = TextInput(
            font_size=45,
            size_hint_y=.2,
            readonly=True,
            halign="right",
            multiline=False,
            background_normal="",
            background_active="",
            background_color=SAKURA,
            foreground_color=VINO,
        )
        self.add_widget(self.result)

        #Buttons

        buttons = [
            ['C', '<', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]
        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for cell in row:
                background = SAKURA
                text_color = VINO

                if cell in ['+', '-', '*', '/', '%']:
                    background = PINK
                elif cell in ['C', '<']:
                    background = SEQUOIA
                    text_color = (1, 1, 1, 1)
                elif cell == '=':
                    background = SCARLET
                    text_color = (1, 1, 1, 1)

                button = Button(
                    text=cell,
                    font_size=32,
                    on_press=self.button_pressed,
                    background_normal="",
                    background_color=background,
                    color=text_color,
                )
                grid.add_widget(button)
        self.add_widget(grid)

# methods

    def button_pressed(self, instance):
        text = instance.text

        if text == 'C':
            self.result.text = ""
        elif text == '=':
            self.calculate()
        elif text == "<":
            self.result.text = self.result.text[:-1]
        elif text == "%":
            self.convert_procent()
        else:
            self.result.text += text

    # calculate
    def calculate(self):
        try:
            self.result.text = str(eval(str(self.result.text)))
        except Exception:
            self.result.text += 'ERROR'

    def convert_procent(self):
        try:
            self.result.text = str(float(str(self.result.text))/100)
        except ValueError:
            self.result.text += 'ERROR'
class CalculatorApp(App):
    def build(self):
        return Calculator()
if __name__ == '__main__':
    CalculatorApp().run()
