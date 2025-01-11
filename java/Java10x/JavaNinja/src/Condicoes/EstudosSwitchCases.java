package TiposDeDados;

import java.util.Scanner;

public class EstudosSwitchCases {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Escolha um personagem: ");
        System.out.println("1 - Naruto Uzumaki");
        System.out.println("2 - Sasuke Uchiha");
        System.out.println("3 - Sakura Haruno");

        int escolhaDoUsuario = sc.nextInt();

        switch (escolhaDoUsuario){
            case 1:
                System.out.println("O usuario escolheu o Naruto Uzumaki");
                break;
            case 2:
                System.out.println("O usuario escolheu o Sasuke Uchiha");
                break;
            case 3:
                System.out.println("O usuario escolheu a sakura haruno");
                break;
            default:
                System.out.println("Invalido");
        }




    }
}
