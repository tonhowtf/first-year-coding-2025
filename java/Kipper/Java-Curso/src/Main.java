import java.util.ArrayList;

public class Main {


    public static void main(String[] args) {
        Carro meuCarro = new Carro("Fusca");
        Carro meuCarro1 = new Carro("Bruno");
        Carro meuCarro2 = new Carro("Laborinho");

    }

}

class Carro {
    String modelo;
    public Carro(String modelo){
        this.modelo = modelo;
    }
    public void acelerar(){
        System.out.println("Acelerar");
    }
}
