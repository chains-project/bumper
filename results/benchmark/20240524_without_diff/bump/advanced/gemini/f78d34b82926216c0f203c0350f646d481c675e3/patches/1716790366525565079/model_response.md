```java
import ml.peya.plugins.Objects.Decorations;
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public static void main(String[] args) {
        WaveCreator waveCreator = new WaveCreator();
        waveCreator.createWaveFile(args[0], args[1]);
    }
}
```