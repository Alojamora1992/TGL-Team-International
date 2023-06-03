def parametros(primer, segundo, tercer, cuatro="Soy el valor por defecto"): # Cuatro tiene por defecto el valor "Soy el valor por defecto"
    print(primer, segundo, tercer, cuatro)

parametros("Primero", "Segundo", "Tercer")
parametros("Primero", tercer="Tercero", segundo="Segundo", cuatro="Cuatro")