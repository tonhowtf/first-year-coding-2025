package polimorfismo_abstracao_igual_coracao;

public abstract class Ninja implements EstrategiaDeBatalha {

    String nome;
    String aldeia;
    int idade;

    //TODO: Incluir 2 novos atributos: numeroDeMissõesConcluidas, Rank

    public Ninja(){

    }

    public Ninja(String nome, String aldeia, int idade) {
        this.nome = nome;
        this.aldeia = aldeia;
        this.idade = idade;
    }

    // Metodos gerais!
    public void habilidadeEspecial() {
        System.out.println("Meu nome é " + nome + "e esse é o meu ataque especial");

    }
    @Override
    public void estrategiaDeBatalhaNinja() {
        System.out.println("Essa é minha estrategia de combate");
    }

}
