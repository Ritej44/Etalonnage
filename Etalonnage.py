def extraction(fichier):
    valeur_total = 0 
    with open(fichier, 'r') as file:
      for line in file:
        Numero=[char for char in line if char.isdigit()]
        if Numero:
              num1=Numero[0]
              num2=Numero[-1]  
              val_etalonnage=int(num1+num2)         
              valeur_total += val_etalonnage
        
    return valeur_total


fichier="C:/Users/Ritej/Downloads/document.txt"
valeur_total=extraction(fichier)
print("La somme des valeurs d'étalonnage est : ",valeur_total)


