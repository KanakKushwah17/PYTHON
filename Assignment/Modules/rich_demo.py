from rich import print

#structure  [style]text[/style]

#Colors add 
print("[red]Hello,world![/red]")
print("[green]Success[/green]")



#Style text BOLD
print("[bold]This is bold[/bold]")
 

#ITALIC
print("[italic]This is italic [/italic]")


#Underlined
print("[underline]This is underlined[/underline]")


#Combine styles
print("[bold red]Critical Error[/bold red]")

"""
---------------------------Important Styles to Remember--------------------------------
red
green
blue
yellow
cyan
magenta
bold
italic
underline
-----------------------------------------------------------------------------------------

"""

from rich.console import Console
console = Console()

#Line and write between the lines 
console.rule("Python")# make ----- line ---------- use in CLI applications.


from rich.table import Table
table=Table()

# using for title 
table = Table(title="Student Details")



#Add column in a table 
table.add_column("Name")
table.add_column("Age")
table.add_column("City")

# ADD row in a table
table.add_row("Rahul", "21", "Indore")
table.add_row("Amit", "22", "Bhopal")
table.add_row("Priya", "20", "Pune")

console.print(table)






#------------------------------------PANEL--------------------------------------------
from rich.panel import Panel
console = Console()
console.print(Panel("Website is SAFE"))#------------In a box---------------------------
console.print(Panel("Website is SAFE",title="CYBERLENS"))#------BOX WITH TITLE---------








#-----------------------------------Progress Bar-------------------------------------
from rich.progress import track
import time

for i in track(range(100), description="Processing..."):
    time.sleep(0.05)

#This gives you a visual progress indicator.









#---------------------------------Console status-----------------------------------------
with console.status("Processing..."):
    time.sleep(1)

console.print("[green]Done![/green]")
#Sometimes you don't know exactly how much work is remaining.












#----------------------------------console input-------------------------------------------

name = console.input("[bold green]Enter your name: [/bold green]")

console.print(f"Hello, {name}")
# for input using console rich


















#-----------------------------------Console.log-------------------------------------
console.log("Program started")
console.log("Connecting to database")
console.log("Data loaded")
#log() = information for the developer about what the program is doing.


















#------------------------------------------Pretty trackbacks---------------------------
"""from rich.traceback import install

install()

x = 10 / 0"""
# This is particularly useful while debugging.









#---------------------------------------MARKDOWN--------------------------------------
from rich.markdown import Markdown


text="""
Python is a programming language 
**RICH** makes terminal applications beautiful

"""
console.print(Markdown(text))









#------------------------------------JSON-----------------------------------------------
from rich.json import JSON
data='{"name":"kanak","language":"Python"}'
console.print((JSON(data)))




