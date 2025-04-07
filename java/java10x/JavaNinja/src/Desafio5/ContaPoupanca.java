package Desafio5;

public class ContaPoupanca extends ContaBancaria{
    @Override
    public void depositar(double valor) {
        super.depositar(valor);
        saldo += valor - valor * 0.01;
    }
}
