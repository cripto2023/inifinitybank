from banco import obterConta, banco


def transferir(contaOri: int, contaDes:, int, valor: float) -> None:
    contaOri = obterConta(contaOri)
    contaDes = obterConta(contaDes)
    if contaOri and contaDes:
        if contaOri['saldo'] >= valor:
            contaOri['saldo'] -= valor
            contaDes['saldo'] += valor
            print('Transferencia realizada com sucesso!')
        else:
            print('Saldo insuficiente')
    else:
        print('uma conta não existe')





if __name__ == '__main__':
