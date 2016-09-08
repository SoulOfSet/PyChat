from netobj import TerminalClient
from env import WindowManager
import tkinter as tk

print("PyChat_Client.py: Loading the client manager")



client = TerminalClient.TerminalClient()

client.connect()