import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

import ggt_euklid

# Das GUI-Layout kann geändert werden, indem controller_NestedGrid.kv oder 
# controller_PlainGrid.kv, etc. auf controller.kv KOPIERT wird.

class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    # label_results = ObjectProperty()
    # label_debug = ObjectProperty()
    # text_input1 = ObjectProperty(None)
    # text_input2 = ObjectProperty(None)
    info = StringProperty()

    def do_action(self):
        valid_input = True

        print("1. Wert: ", self.text_input1.text, ", 2. Wert: ", self.text_input2.text)
        if self.toggle_debug.state == 'down':
            self.label_debug.text = "Debug Infos: "
            self.label_debug.text += "1. Wert: " + self.text_input1.text + ", 2. Wert: " + self.text_input2.text
        else:
            self.label_debug.text = ""

        # Ergebnisberechnung (lineare und rekursive Variante)
        # Try .. catch Fehlerbehandlung um Input
        try:
            if self.toggle_variante.state == 'down':
                self.label_results.text = str(ggt_euklid.euklid_recursive(int(self.text_input1.text), int(self.text_input2.text)))
            else:
                self.label_results.text = str(ggt_euklid.euklid(int(self.text_input1.text), int(self.text_input2.text)))
        except ValueError:
            valid_input = False
            print("WARNING: Wrong input values. Integer values only!")
            Controller.do_clear(self)
            self.label_debug.text = "WARNING: Wrong input values. Integer values only!"

        if valid_input:
            print(" -> Ergebnis: ", self.label_results.text)
            if self.toggle_debug.state == 'down':
                self.label_debug.text += " -> Ergebnis: " + self.label_results.text
                self.label_debug.text += "\nToggle_Debug: " + self.toggle_debug.state + ", Toogle_Variante: " + self.toggle_variante.state

                if self.toggle_variante.state == 'down':
                    self.label_debug.text += "\nRekursive Variante"
                else:
                    self.label_debug.text += "\nIterative Variante"

    # Clear input values
    def do_clear(self):
        self.text_input1.text = "0"
        self.text_input2.text = "0"
        self.label_results.text = ""
        self.label_debug.text = ""


class ControllerApp(App):

    def build(self):
        return Controller(info='GGT-Berechnung')

if __name__ == '__main__':
    ControllerApp().run()
