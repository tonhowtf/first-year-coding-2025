package polimorfismo_abstracao_igual_coracao;

public class Main {
    public static void main(String[] args) {

        //Obj Uchiha
        Uchiha sasuke = new Uchiha();
        sasuke.nome = "Sasuke Uchiha";
        sasuke.aldeia = "Aldeia da folha";
        sasuke.idade = 18;
        sasuke.habilidadeEspecial();

        //Obj Uchiha 2
        Hatake kakashi = new Hatake();
        kakashi.nome = "Kakashi Hatake";
        kakashi.aldeia = "Aldeia da folha";
        kakashi.idade = 48;
        kakashi.sharinganAtivado();
        kakashi.bemVindoAAnbu();
        kakashi.hokageAtivo();




    }
}
