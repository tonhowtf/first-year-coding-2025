package Desafio5;

public abstract class ContaBancaria implements Conta {

    Double saldo;

    @Override
    public void consultarSaldo() {
        System.out.println("Seu saldo é: " + saldo);
    }
    public void depositar(double valor) {
        valor += saldo;
    }
}
