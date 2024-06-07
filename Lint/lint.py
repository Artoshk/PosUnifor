import time

def main():
    print("Imagine que ele tá rodando o lint")
    for i in range(10):
        time.sleep(0.1)
        print('.', end='', flush=True)
    print()
    print("Lint finalizado com sucesso")

if __name__ == '__main__':
    main()
