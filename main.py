import matplotlib.pyplot as plt
import pandas as pd


def main():
    read_pandas();

def read_pandas () -> None:
    try:
        dict = {
            "x": [],
            "y": []
         }
        df = pd.read_excel("C:\Treinamentos\python-task\estimativa.xls")        
        
        group = df.groupby(by="UF")["POPULACAO"].apply(list)
        
        for i in group.items():
          title = i[0] 
          counter = sum(i[1])
          
          dict["x"].append(title)
          dict["y"].append(counter)
          
        generate_garph_plot(dict["x"], dict["y"]) 
        generate_garph_bar_vert(dict["x"], dict["y"]) 
        generate_garph_bar_hori(dict["x"], dict["y"]) 
          

    except Exception as ex:
       print(ex)   
 
def generate_garph_plot(x, y) -> None:
    plt.plot(x, y)
    set_name(plt)
    plt.show()  
        
def generate_garph_bar_vert(x, y) -> None:
    plt.bar(x, y, color= "red")
    set_name(plt)
    plt.show()  
    
def generate_garph_bar_hori(x, y) -> None:
    plt.barh(x, y, color= "blue")
    set_name(plt)
    plt.show()  

def set_name(pypl):
    pypl.title('Estimativa populacional de municipios.')
    pypl.xlabel('Estado')
    pypl.ylabel('Estimativa')
    
main();
 