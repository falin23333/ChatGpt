
from rich import print
from rich.table import Table


import time
from rich.progress import track
API_KEY = "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"

logo = """
                                                                                                                                               ████

██████╗██╗  ██╗ █████╗ ████████╗     ██████╗ ██████╗ ████████╗    ██████╗    ███████╗    ██████╗ ██╗   ██╗    ██╗  ██╗███████╗██╗   ██╗     ███╗   ██╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██╔════╝ ██╔══██╗╚══██╔══╝    ╚════██╗   ██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██║ ██╔╝██╔════╝╚██╗ ██╔╝     ████╗  ██║
██║     ███████║███████║   ██║       ██║  ███╗██████╔╝   ██║        █████╔╝   ███████╗    ██████╔╝ ╚████╔╝     █████╔╝ █████╗   ╚████╔╝█████╗██╔██╗ ██║
██║     ██╔══██║██╔══██║   ██║       ██║   ██║██╔═══╝    ██║        ╚═══██╗   ╚════██║    ██╔══██╗  ╚██╔╝      ██╔═██╗ ██╔══╝    ╚██╔╝ ╚════╝██║╚██╗██║
╚██████╗██║  ██║██║  ██║   ██║       ╚██████╔╝██║        ██║       ██████╔╝██╗███████║    ██████╔╝   ██║       ██║  ██╗███████╗   ██║        ██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝        ╚═╝       ╚═════╝ ╚═╝╚══════╝    ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═╝  ╚═══╝
                                                                                                                                                       
██╗   ██╗███████╗██████╗      ██╗    ██████╗                                                                                                           
██║   ██║██╔════╝██╔══██╗    ███║   ██╔═████╗                                                                                                          
██║   ██║█████╗  ██████╔╝    ╚██║   ██║██╔██║                                                                                                          
╚██╗ ██╔╝██╔══╝  ██╔══██╗     ██║   ████╔╝██║                                                                                                          
 ╚████╔╝ ███████╗██║  ██║     ██║██╗╚██████╔╝                                                                                                          
  ╚═══╝  ╚══════╝╚═╝  ╚═╝     ╚═╝╚═╝ ╚═════╝                                                                                                           
                                                                                                                                                       
"""
ia = """
 #*#**#*#*##*#**#****#***++++++++++++++++*++=++*++++++**+++**+***+*#*********##*##*####*%#
%%%%%%%%%%%%#%%##########*#*************+**+++++++***************#*##########%%#%%%%%%%%%%
*####***##*#****#*+++**++++=+++++=======++********+====+++=+*+++++++**+*******#**#****#*#%
%%%%%%%%%%%%############*******++++*##%@@@@@@@@@@@@@%%*+++**********#############%%%%%%%%%
#####**##*#****#*++++*++++=+===+*%@%%@@@@@@@@@@@@@@@@@@@#+=++++++++*++*******#*******###%#
%%%%#%#%%########*********++=*%#*###*#%#%@@@@@@@%#*#%%%%%@#+++*+**********##########%%%%%%
#####*****#******++++*+++===##*#%@@@@%#*%@@@#*####%%##**%@@%==++++++++++**+**********#*#%#
%%%%#####*##*#*#*******++==%%*%@@@%%%@@%**%@##%@@@@@@@@%###%%=+++++**********##*########%%
######********+*+*++=+++==#%**@@@#%%#@@@*%#*#@@@@%%%%@@@@#*%@*==++++++++++*************#*#
%#%#%######*#******+*+*++=%@@##@@@@@@@@#*##*%@@@#*####@@@@*%@#=++++++********#*##*#######%
#**#********+*++*==+=*===-%@@####%%%%###%%%*%@@@%*##*%@@@%**%%-====++++++++++**+********%*
%%%%########*#********+++=#@@@@@%*#%%##%@%#*#%@@@@@@@@@@%##%%%==++++++********#*########%%
+*##*******++*+*++++++++===%@@@@@@@%###%###%%*%%@@@@@@%%*#@@@#======++++*+++++++*****#****
%%#%########*#********+++==%@@@@@@%#%@%%%@%*%**##########%@@@+=+++++++********#*########%%
%###********+*+**++++*+==-=@@@@@@@%*%@%##@@*#@@@@@##%@@@@@@@#-==+=+++++++++++***********%#
%%##%#####*##*********++=+%@@@@@@@@##%@@@%##@@@@@@@@@@@@@@@%==++++++********#*##*########%
###%#***#**#*+**#++=+++=#@@@@@@@@@@@%#%##%%@@@@@@@@@@@@@@@@*==+++++++++++++***#******##*#%
#%########*#**#******++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=+++++++*+***********########%
#%#########***#*******+=+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=++++++**+**********##*#####%#
%####%####*#*#********+++=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==+++*+***********#*######%###
%%###%%########***#*****+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=+**********#*##########%%%%#
##%##*########*#**+*****++=*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++++*********##*##########%##
%%%%%%#%%#%####%###*####***+=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++***##########%##%%%%%%#%%%
####%##**##*#*#**%********+++*%@@@%###**++#@@@@@@@@@@@@@@@@@@@%++++*******#*##*###########
##%%%%#%#%%#%%#######*####***+*+++++++*+*+=#@@@@@@@@@@@@@@@@@@@%#+*#*#####%##%#%%#%%%##%


"""
def TABLA():
    mi_tabla = Table("Comandos","Descripcion")
    mi_tabla.add_row("!exit","Cierra el chat guardando la conversaciòn")
    mi_tabla.add_row("!new","Abre un nuevo chat sin guardar y sin recordar")
    
    mi_tabla.add_row("!special","Ejecuta una funcion especial que hayas programado")
    print(f"[bold blue]{logo}[/bold blue]")
    print(f"[bold cyan]{ia}[/bold cyan]")
    print(mi_tabla)
    

    for _ in track(range(20), description="Recordando Conversacion anterior..."):
        time.sleep(0.1)  # Simulate work being done

def new_conversation():
    
    messages =  [{"role":"system","content":"You are a cryptocurrency expert"}]
    print("[bold red] Inicializando CHAT GPT 3 💗.... [/bold red]")
    return messages,input("¿De què te gustaría hablar ahora? :\n\n")


def GrabarConsersacion(messages,writer):
    for row in messages:
        writer.writerow(row)
     