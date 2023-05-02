# ---> sys
import os

# ---> Modules Rich
from rich.panel import Panel
from rich import print
from rich.console import Console
console = Console()


# ---> MainStart
if __name__=="__main__":
#  try:os.system("main/python .ex.py")
  try:os.system("python .ex.py")
  except requests.exceptions.ConnectionError as e:
      Console(width=70).print(Panel(f'''{str(e).title()}''',style=f"bold white",padding=(0,4)))
      sys.exit()
