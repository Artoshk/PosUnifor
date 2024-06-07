import time

def main():
    print("Imagine que ele tá rodando o lint e os testes")
    for i in range(10):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()
    print("Lint e testes finalizados com sucesso")

if __name__ == '__main__':
    main()
