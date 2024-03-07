import analex

input_path = '../in/in.txt'
res_path = '../res/resultado.txt'

def reader():
    str = open(input_path, 'r').read()
    return str

def writer(output):
    out = open(res_path, 'w')
    out.write(output)

def main():
    input = reader()
    writer(analex.ana(input))

if __name__ == "__main__":
    main()