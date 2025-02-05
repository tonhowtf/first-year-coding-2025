package Desafio03;

public class Uchiha extends Ninja{
    String HabilidadeEspecial;
    String mostrarHabilidadeEspecial(){
        return HabilidadeEspecial;
    }
    public void MostrarInformações(){
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Missão: " + missão);
        System.out.println("Habilidade Especial: " + HabilidadeEspecial);
    }
}
