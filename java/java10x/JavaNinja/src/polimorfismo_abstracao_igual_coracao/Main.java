package polimorfismo_abstracao_igual_coracao;

public class Main {
    public static void main(String[] args) {

        System.out.println("Naruto");

        Uzumaki naruto = new Uzumaki("naruto", "Aldeia da folha", 16);
        System.out.println(naruto);
        System.out.println("----");
        naruto.tacarKunai();
        System.out.println("----");

        System.out.println("Sasuke");
        Uchiha sasuke = new Uchiha("Sasuke", "Aldeia da folha", 18);




    }
}
