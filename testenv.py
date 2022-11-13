import os
from dotenv import load_dotenv
import ctypes


load_dotenv()



print(os.getenv("DB_NAME"))
# * obtener el size de la pantalla

user32 = ctypes.windll.user32
user32.SetProcess
