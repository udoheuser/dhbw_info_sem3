from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    # Initialisation of private attributes a and b
    self.__a = 0
    self.__b = 0
    
    # 4. Ausbaustufe: Initioalisierung der Euklidschen Variante
    self.__recursive_variante = False

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # 1. Ausbaustufe: try .. except .. else um int(text_box)
    try:
      self.__a = int(self.text_box_1.text)
      self.__b = int(self.text_box_2.text)
    except:
      print("Falsche Eingabe: Verwenden Sie bitte ganze Zahlen!")
      # 2. Ausbaustufe: Zusätzliche Fehlermeldung auf label_err_msg
      self.__err_msg = "Falsche Eingabe: Verwenden Sie bitte ganze Zahlen!"
      print(self.__err_msg)
      self.label_err_msg.text = self.__err_msg
      self.label_err_msg.foreground = "red"
    else:
      # 4. Ausbaustufe: Wechsel zw. rec. und iterat. Variante
      if self.__recursive_variante:
        return_value = anvil.server.call("ggt_euklid_recursive", self.__a, self.__b)
      else:
        return_value = anvil.server.call("ggt_euklid", self.__a, self.__b)

      self.label_result.text = str(return_value)
      # 3. Ausbaustufe: Löschen der alten Fehlermeldung
      self.label_err_msg.text = ""
      self.label_err_msg.foreground = "black"

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.check_box_1.checked:
      self.__recursive_variante = True
    else:
      self.__recursive_variante = False

'''
Weitere Ausbaustufen: 
5. Einführung eines Clear-Buttons, welcher Ein-, Ausgaben und Fehler-
   meldungen resettet (löscht)
6. Anpassung des Designs inkl. DHBW-Logo, Copyright, Impressum, etc.
7. Messung der unterschiedlichen Berechnungszeiten und Ausgabe auf Label
   (out of scope!)
'''
