package NivelIntermediario;

public class Main {
    public static void main(String[] args) {

        Ninja Naruto = new Ninja();

        Naruto.nome = "Naruto Uzumaki";
        Naruto.aldeia = "Aldeia da Folha";
        Naruto.idade = 18;

        // Sasuke

        Ninja Sasuke = new Ninja();

        Sasuke.nome = "Sasuke Uchiha";
        Sasuke.aldeia = "Aldeia da Folha";
        Sasuke.idade = 18;

        // Aplicando Métodos aos meus objetos:
        Sasuke.SharinganAtivado();
        System.out.println(Sasuke.EuSouNinja());

        // Sakura

        Ninja Sakura = new Ninja();

        Sakura.nome = "Sakura Haruno";
        Sakura.aldeia = "Aldeia da Folha";
        Sasuke.idade = 18;
    }


}
