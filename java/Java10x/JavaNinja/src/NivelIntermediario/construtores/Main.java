package NivelIntermediario.construtores;

public class Main {
    public static void main(String[] args) {


        Hokages Hashirama = new Hokages("Hashirama");
        Hashirama.idade = 45;

        Hokages Tobirama = new Hokages("Tobirama");
        System.out.println(Tobirama.nome);

        Hokages Hiruzen = new Hokages(45);


    }
}
