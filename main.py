def echo(w, n):
    output = w
    for i in range (0, n-1):
        output = output + w
    return output

print (echo("echo", 3))