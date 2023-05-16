from Conversion_Sciensano.conversion import jsonConversion
from Espérance_de_maximisation.EM import execute_em_algorithm


def main():
    jsonConversion("dataBrutSciensano.json")
    execute_em_algorithm('dataEM.json')


if __name__ == "__main__":
    main()
