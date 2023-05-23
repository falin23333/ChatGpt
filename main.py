 # https://platform.openai.com/docs/models/overview , here you can see all models 
import typer
import openai
import config
import typer
from rich import print

from io import open
import csv



def main():
    
    flag = 0
    openai.api_key = config.API_KEY # cargo mi api_key OpenAI
    messages =[{"role":"system","content":"Quiero que me ayudes"}] # Pongo al bot en un contexto inicial
    
   ############################# Abro Fichero csv para recordar al bot ####################################
    
    with open("MEM_chatGPT.csv", newline="\n") as csvfile:
        reader = csv.DictReader(csvfile,delimiter = ",")
        for i,linea in enumerate(reader):
            if i !=0: # Evito leer otra vez la primera linea {"role":"system","content":"Eres un gran asistente"},cagrada ya en messages
                messages.append(linea) 
    #######################################################################################################
    
    ####################################### Imprimo Comandos internos #####################################
    config.TABLA()
    #######################################################################################################
     
    ####################################### Empieza la conversacion con el bot ############################
    content = input("Que quieres saber :\n\n> ")
    while content != "!exit":
        
    
        if content == "!new":
            flag = 1
            messages.clear()
            messages,content= config.new_conversation()

        elif content == "!special":
            
            for i in range (1,57,1):
                content = f"Define Bitcoin en {i} palabras"
                messages.append({"role":"user","content":content})                      # guardo mis preguntas ROLE USER para que sepa que le preguntñe anteriormente
                response = openai.ChatCompletion.create(
                                    model= "gpt-3.5-turbo",              
                                    messages = messages                         # cuanto mas iteracione el bucle mas conocimiento tendra de lo que le estamos hablamdo
                                    )
                response_content = response.choices[0].message.content                  #guardo sus respuestas ROLE ASSISTANT para que  sepa que ha respondido 
                messages.append({"role":"assistant","content":response_content})
                print(f"[bold blue]{i}: {response.choices[0].message.content} [/bold blue]")
                
        else:       
            messages.append({"role":"user","content":content})                      # guardo mis preguntas ROLE USER para que sepa que le preguntñe anteriormente
            response = openai.ChatCompletion.create(
                                        model= "gpt-3.5-turbo",              
                                        messages = messages                         # cuanto mas iteracione el bucle mas conocimiento tendra de lo que le estamos hablamdo
                                        )
            response_content = response.choices[0].message.content                  #guardo sus respuestas ROLE ASSISTANT para que  sepa que ha respondido 
            messages.append({"role":"assistant","content":response_content})
            print(f"[bold blue] {response.choices[0].message.content} [/bold blue]")
            
      

       
        content = input("> ")
    

    

    with open("MEM_chatGPT.csv","w", newline="\n") as csvfile:
        writer = csv.DictWriter(csvfile,delimiter = ",",fieldnames=["role","content"])
        writer.writeheader()
        config.GrabarConsersacion(messages,writer)
    print("[bold red] Grabando Conversacion💗.... [/bold red]")
    




if __name__ == "__main__":
    typer.run(main)