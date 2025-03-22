package NivelIntermediario;

public class Main {
    public static void main(String[] args) {

        //Objeto 1
        Uzumaki naruto = new Uzumaki();
        naruto.ModoSabioAtivado();
        naruto.nome = "Naruto Uzumaki";
        naruto.aldeia = "Aldeia da folha";
        naruto.idade = 17;

        //Objeto 2
        Uchiha sasuke = new Uchiha();
        sasuke.nome = "Sasuke Uchiha";
        sasuke.aldeia = "Aldeia da folha";
        sasuke.idade = 18;
        sasuke.SharinganAtivado();

        //Objeto 3
        Haruno sakura = new Haruno();
        sakura.nome = "Sakura Haruno";
        sakura.aldeia = "Aldeia da folha";
        sakura.idade = 16;

        //Objeto 4
        Ninja Hinata = new Ninja();
        Hinata.nome = "Hinata Hyuga";
        Hinata.aldeia = "Aldeia da folha";
        Hinata.idade = 17;
    }


}
