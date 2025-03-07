# Programa que dibuja un corazón más estético con colores
from termcolor import colored

def print_heart():
    print(colored('''
          💗💗💗       💗💗💗
       💗💗💗💗💗💗   💗💗💗💗💗💗
     💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
    💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
   💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
   💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
    💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
     💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
       💗💗💗💗💗💗💗💗💗💗💗💗
         💗💗💗💗💗💗💗💗💗💗
           💗💗💗💗💗💗💗💗
             💗💗💗💗💗💗
               💗💗💗💗
                 💗💗
                  💗
    ''', 'red'))

def main():
    print_heart()
    print(colored("\n¡Te amo Python! 💖", 'magenta', attrs=['bold']))

if __name__ == "__main__":
    main()