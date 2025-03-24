package Construtores;

public class Main {
    public static void main(String[] args) {
        Hokages Hashirama = new Hokages();
        Hokages Tobirama = new Hokages("Tobirama");
        Hokages Hiruzen = new Hokages(40);
        Hokages Minato = new Hokages("Minato Namikaze", 32, false);
        Hashirama.idade = 45;
    }
}
