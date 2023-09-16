def hello():
    from foo import API_KEY

    return f'hello{API_KEY}'

#pt circular imports = importul se face la nivel de functie si va functiona (importi dupa definirea functiei)