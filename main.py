from Conversion_Sciensano.conversion import jsonConversion
from Espérance_de_maximisation.EM import execute_em_algorithm


def main():
    jsonConversion()
    execute_em_algorithm()


if __name__ == "__main__":
    main()
