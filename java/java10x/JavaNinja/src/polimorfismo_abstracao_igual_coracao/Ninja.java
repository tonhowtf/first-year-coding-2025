package polimorfismo_abstracao_igual_coracao;

public abstract class Ninja implements EstrategiaDeBatalha {

    String nome;
    String aldeia;
    int idade;
    int numeroDeMissoesConcluidas;
    NivelNinja rank;

    //TODO: Incluir 2 novos atributos: numeroDeMissõesConcluidas, Rank
    // TODO: RANK: Gennin, Chunnin, Jounnin, Hokage

    public Ninja(){

    }

    public Ninja(String nome, String aldeia, int idade) {
        this.nome = nome;
        this.aldeia = aldeia;
        this.idade = idade;

    }

    public Ninja(String nome, String aldeia, int idade, NivelNinja rank, int numeroDeMissoesConcluidas) {
        this(nome, aldeia, idade);
        this.numeroDeMissoesConcluidas = numeroDeMissoesConcluidas;
        this.rank = rank;
    }

    // TODO: Sobrecarga do construtor chamando os novos atributos

}
