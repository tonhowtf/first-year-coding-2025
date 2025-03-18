package NivelIntermediario;

public class Ninja {
    String nome;
    String aldeia;
    int idade;

    public void SharinganAtivado(){
        System.out.println("Sharingan ativado");
    }

    public String EuSouNinja() {
        return "Oi, Eu sou um ninja!";
    }

    public int anosParaSeTornarHokage(int idadeMinimaParaSerHokage) {
        return idadeMinimaParaSerHokage - idade;

    }
}


