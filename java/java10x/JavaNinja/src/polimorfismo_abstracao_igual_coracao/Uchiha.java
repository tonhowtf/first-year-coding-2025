package polimorfismo_abstracao_igual_coracao;

public class Uchiha extends Ninja implements SharinganInterface {

    public Uchiha() {
        super();
    }

    public Uchiha(String nome, String aldeia, int idade) {
        super(nome, aldeia, idade);
    }

    public Uchiha(String nome, String aldeia, int idade, int numeroDeMissoesConcluidas, NivelNinja rank) {
        super(nome, aldeia, idade,numeroDeMissoesConcluidas, rank);
    }


    @Override
    public void estrategiaDeBatalhaNinja() {

    }

    @Override
    public void inteligenciaDeCombate() {
        System.out.println("Meu nome é " + nome + "e essa é a minha inteligencia de combate");
    }

    @Override
    public void inteligenciaDeCombate(int qi) {

        if(qi > 150) {
            System.out.println("Seu QI é: " + qi + " e você é um genio");
        } else if (qi >= 130) {
            System.out.println("Seu QI é: " + qi + " e você é um ninja promissor");
        } else {
            System.out.println("Seu QI é:" + qi + " e você precisa treinar mais suas estrategias");
        }
    }


    @Override
    public void sharinganAtivado() {

    }
}
