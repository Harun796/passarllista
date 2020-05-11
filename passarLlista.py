import os
from datetime import date

directoriMatricula="matricula"
directoriAssistencia="assistencia"
directoriGrups="grups"


opcioMenu =0
while (opcioMenu !=5):
  print("1- Configurar sistema")
  print("2- Fer fulls de grup")
  print("3- Passa llista")
  print("4- Consultar assistència")
  print("5- Sortir")
  opcioMenu = int(input("Entra opció"))
  if(opcioMenu == 1):
      while(os.path.isdir(directoriMatricula)!= True ):
          directoriMatricula = input("A quin directori està alumnat.csv")
      while(os.path.isdir(directoriAssistencia)!= True ):
          directoriAssistencia = input("A on posaras l'assistencia")
      while(os.path.isdir(directoriGrups)!= True ):
          directoriGrups = input("A on posras els grups")    
  if(opcioMenu == 2):
    fitxer = open(directoriMatricula+"/alumnat.csv","r")
    #Obres arxius
    E1= open(directoriGrups+"/ESO1.csv","w",newline="")
    E2= open(directoriGrups+"/ESO2.csv","w")
    E3= open(directoriGrups+"/ESO3.csv","w")
    E4= open(directoriGrups+"/ESO4.csv","w")
    B1= open(directoriGrups+"/BAT1.csv","w")
    B2= open(directoriGrups+"/BAT2.csv","w")

    contingut = fitxer.readline()
    for i in fitxer:
      linia=i.split(",")
      if(linia[1]=="11" or linia[1] == "12"):
        E1.write(linia[0] +","+linia[2]+","+linia[5])
      elif(linia[1]=="13"):
        E2.write(linia[0] +","+linia[2]+","+linia[5])
      elif(linia[1]=="14"):
        E3.write(linia[0] +","+linia[2]+","+linia[5])
      elif(linia[1]=="15"):
        E4.write(linia[0] +","+linia[2]+","+linia[5])
      elif(linia[1]=="16" ):
        B1.write(linia[0] +","+linia[2]+","+linia[5])
      elif(linia[1]=="18"or linia[1]=="17"):
        B2.write(linia[0] +","+linia[2]+","+linia[5])
    E1.close()
    E2.close()
    E3.close()
    E4.close()
    B1.close()
    B2.close()
  elif(opcioMenu == 3):
    curs = input("Quin curs vols passar llista")
    today = date.today()
    cursFitxer = open(directoriGrups+"/"+curs+".csv","r")
    llistacurs = open(directoriAssistencia+"/"+curs+str(today)+".csv","w")
    for f in cursFitxer:
      #trasnformar la f a llista
      linia2=f.split(",")
      print(linia2[0])
      assis=(input("Si l'alumne està posa un 1 i si no està posa un 0"))
      llistacurs.write(linia2[0]+assis+"\n")
    cursFitxer.close()
    llistacurs.close()
  elif(opcioMenu == 4):
    fitxer = os.listdir(directoriAssistencia)
    for nomFitxer in fitxer:
      print(nomFitxer)
    obrir= input("Quin directori vols obrir")
    consultar=open(directoriAssistencia+"/"+obrir ,"r")
    for e in consultar:
      z=e.replace("0"," Falta!").replace("1"," ")
      print(z)
      


      

      #Escrius  en format csv nom,edat,email,mobil    #Tanques
print("Adéu bon dia tinguis!")