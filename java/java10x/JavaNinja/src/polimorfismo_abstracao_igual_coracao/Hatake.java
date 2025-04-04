package polimorfismo_abstracao_igual_coracao;

public class Hatake extends Ninja implements SharinganInterface {

    public void boasVindas(){
        System.out.println(nome + ": Eu sou um Hatake");
    }

    public void sharinganAtivado() {
        System.out.println("Ativou o Sharingan");
    }
}
