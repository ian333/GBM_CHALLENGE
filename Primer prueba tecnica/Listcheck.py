def locator():
    
    lista=['a','b','c','d']
    search_elements=['a','b','f']
    boolean_results=[]
    boolean=False

    print(f"Se buscara en la siguiente lista {lista} estos elementos {search_elements} ")
    for i in search_elements:
        for j in lista:
            if i == j:
                boolean=True
                break
            else:
                boolean=False
        boolean_results.append(boolean)
    
    for i in range (0,len(search_elements)):
        print(f"¿El elemento {search_elements[i]} se encuentra en la lista? {boolean_results[i]}")


