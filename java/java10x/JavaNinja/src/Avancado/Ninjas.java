package Avancado;

public class Ninjas {

    String nome;
    int idade;

    public Ninjas(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Ninjas{" +
                "nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}
