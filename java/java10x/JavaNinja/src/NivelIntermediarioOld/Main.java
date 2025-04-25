package NivelIntermediarioOld;

public class Main {
    public static void main(String[] args) {

        //Objeto 1
        Uzumaki naruto = new Uzumaki();
        naruto.nome = "Naruto Uzumaki";
        naruto.aldeia = "Aldeia da folha";
        naruto.idade = 17;
        naruto.ModoSabioAtivado();

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
        Hyuga hinata = new Hyuga();
        hinata.nome = "Hinata Hyuga";
        hinata.aldeia = "Aldeia da folha";
        hinata.idade = 17;
        hinata.ByakuganAtivado();

        //Objeto 5
        Boruto boruto =  new Boruto();
        boruto.nome = "Boruto Uzumaki";
        boruto.aldeia = "Aldeia da folha";
        boruto.idade = 12;
        boruto.AtivarJougan();

    }


}
