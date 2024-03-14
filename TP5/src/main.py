import sys
import json
import vending

def loader(data_path):
    data_file = open(data_path, 'r')
    data = json.load(data_file)

    return data

def saver(data_path, new_stock):
    data_file = open(data_path, 'w')
    json.dump(new_stock, data_file, indent=2, ensure_ascii=False)

def main(argv):
    data_path = argv[1]
    stock = loader(data_path)

    new_stock = vending.start(stock)

    saver(data_path, new_stock)
    

if __name__ == "__main__":
    main(sys.argv)