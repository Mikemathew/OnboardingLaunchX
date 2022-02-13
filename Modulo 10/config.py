#Ejercicio de manejo de errores

def main():
    try:
        configuration = open('OnboardingLaunchX/Modulo 10/Config.txt')
        print("Termination: OK")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()