package polimorfismo_abstracao_igual_coracao;

public class Uzumaki extends Ninja{

    @Override
    public void habilidadeEspecial() {
        System.out.println("Meu nome é " + nome + "e esse é meu ataque Uchiha");
    }

    public Uzumaki() {
    }

    public Uzumaki(String nome, String aldeia, int idade) {
        super(nome, aldeia, idade);
    }

    public Uzumaki(String nome, String aldeia, int idade, int numeroDeMissoesConcluidas, NivelNinja rank) {
        super(nome, aldeia, idade, numeroDeMissoesConcluidas, rank);
    }

    @Override
    public String toString() {
        return "Esse é o método toString para referencia de memoria";
    }
}
