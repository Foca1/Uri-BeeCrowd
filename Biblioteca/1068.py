def isCorrect(expressao: str):
    todos, parentesesEsq, parentesesDir = [], [], []

    for char in expressao:
        if char == "(" or char == ")":
            todos.append(char)
    
    for parenteses in todos:
        if parenteses == ")":
            parentesesEsq.append(parenteses)
        else:
            parentesesDir.append(parenteses)
        
    if (len(todos)%2) != 0 or todos[-1] == "(" or todos[0] == ")":
        return "incorrect" 
    elif len(parentesesDir) == len(parentesesEsq) and todos[-1] != "(" or todos[0] != ")":
        return "correct"

while True:
    try:
        expressao = input()
        print(isCorrect(expressao))
    except EOFError:
        break
