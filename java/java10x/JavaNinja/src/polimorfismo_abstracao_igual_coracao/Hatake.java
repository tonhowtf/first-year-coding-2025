package polimorfismo_abstracao_igual_coracao;

public class Hatake extends Ninja implements SharinganInterface, AnbuInterface, HokageInterface {

    public void boasVindas(){
        System.out.println(nome + ": Eu sou um Hatake");
    }

    public void sharinganAtivado() {
        System.out.println("Ativou o Sharingan");
    }
    public void bemVindoAAnbu() {
        System.out.println(nome + " Eu sou um ninja de elite da anbu!");
    }
    public void hokageAtivo() {
        System.out.println(nome + ": Eu sou um Hokage");
    }


}
