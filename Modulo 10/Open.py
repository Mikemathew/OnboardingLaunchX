def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print('Error: No existe el archivo')

if __name__ == '__main__':
    main()