import  csv

def ready_up():
    with open('/home/hamid/Downloads/esm_famil_data.csv') as file:
        reader = csv.reader(file)
        for row in reader  : 
            print(row)




ready_up()
