package NivelIntermediario;

public class Shuriken {
    private int tamanho;

    public Shuriken(int tamanho) {
        this.tamanho = tamanho;
    }

    public int getTamanho() {
        return tamanho;
    }

    @Override
    public String toString() {
        return "Shuriken de tamanho: " + tamanho;
    }
}


