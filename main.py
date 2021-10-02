from Listcheck import locator
from days_in_a_month import numberOfDays
from factorial import Factorial
from number_module import module
from sum import suma


def main():
    """
    Esta funcion elige los test que se correran
    """
    test_number = 0
    while test_number != "":
        initial_text = "\n\nBienvenido a los ejercicios del GBM Challenge 😄✌️ \n por favor ingrese el numero del test que desea iniciar \n "
        menu_test = "1: Calcula el Factorial de un numero 🤓\n 2: Buscar 🔍 si un array contiene ciertos elementos \n 3: Hacer la sumatoria ➕ de una lista predefinida\n "
        menu_test_2 = "4: Calcula el Modulo de dos numeros \n 5: Calcula los dias en un mes 📆\n "
        exit_text = "\nSi quiere salir del menu simplemente presione ENTER\n"

        test_number = input(initial_text + exit_text + menu_test+menu_test_2+"Ingresa el numero del test:")
        if test_number == '1':
            num_factorial = int(
                input("Ingrese el numero factorial que quiere calcular "))
            resultado_fact = Factorial(num_factorial)
            print(
                f"El numero {num_factorial} tiene un factorial de {resultado_fact} ")
        elif test_number == '2':
            locator()
        elif test_number == '3':
            suma()
        elif test_number == '4':
            a = int(
                input("Ingrese los dos numeros a los cuales se le extraera el modulo: "))
            b = int(input("Ingrese el dividendo:"))
            module(a, b)
        elif test_number == '5':
            year = int(
                input("Ingrese el año con el que quiere hacer el calculo \n "))
            month = int(
                input("Ingrese el numero del mes del que desea obtener los dias\n "))
            print(f"\n El numero de dias que tiene el mes numero {month} en el año {year} son {numberOfDays(year, month)} dias")


if __name__ == "__main__":
    main()
