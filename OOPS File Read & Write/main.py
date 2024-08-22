with open( 'test.txt') as file:
    content=file.read()
    print(content)

with open('test.txt', mode='a') as file:
    file.write("Hard Work hi")