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

    // TODO NINJA VAI FAZER OBRIGATORIAMENTE
    public void tacarKunai() {
        System.out.println("Tacar Kunai");
    }

    public Ninja(String nome, String aldeia, int idade) {
        this.nome = nome;
        this.aldeia = aldeia;
        this.idade = idade;

    }

    public Ninja(String nome, String aldeia, int idade, int numeroDeMissoesConcluidas, NivelNinja rank) {
        this(nome, aldeia, idade);
        this.rank = rank;
        this.numeroDeMissoesConcluidas = numeroDeMissoesConcluidas;

    }

    // Metodos gerais!
    public void habilidadeEspecial() {
        System.out.println("Meu nome é " + nome + "e esse é o meu ataque especial");

    }
    @Override
    public void estrategiaDeBatalhaNinja() {
        System.out.println("Essa é minha estrategia de combate");
    }

    // Sobrecarga de metodo - Inteligencia de combate
    public void inteligenciaDeCombate() {
        System.out.println("Meu nome é " + nome + "e essa é a minha inteligencia de combate");
    }
    public void inteligenciaDeCombate(int qi) {

        if(qi > 150) {
            System.out.println("Seu QI é: " + qi + " e você é um genio");
        } else if (qi >= 130) {
            System.out.println("Seu QI é: " + qi + " e você é um ninja promissor");
        } else {
            System.out.println("Seu QI é:" + qi + " e você precisa treinar mais suas estrategias");
        }
    }

}
