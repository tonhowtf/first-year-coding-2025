package polimorfismo_abstracao_igual_coracao;

public class Uchiha extends Ninja implements SharinganInterface {

    public Uchiha() {
        super();
    }

    public Uchiha(String nome, String aldeia, int idade) {
        super(nome, aldeia, idade);
    }

    public Uchiha(String nome, String aldeia, int idade, NivelNinja rank, int numeroDeMissoesConcluidas) {
        super(nome, aldeia, idade, rank, numeroDeMissoesConcluidas);
    }


    @Override
    public void estrategiaDeBatalhaNinja() {

    }

    @Override
    public void sharinganAtivado() {

    }
}
