package Condicoes;
import java.util.Scanner;

public class ScannerDoUsuario {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int idadeDoNinja = sc.nextInt();
        if (idadeDoNinja >= 18) {
            System.out.println("Esse ninja já é maior de idade e pode ir para missoes fora da aldeia");
        } else {
            System.out.println("Muito novo");
        }
        sc.close();
    }
}
