```java
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public static WaveCreator waveCreator;

    public Decorations() {
        waveCreator = new WaveCreator(44100, 1.0, 0.0);
    }

    public static WaveCreator getWaveCreator() {
        return waveCreator;
    }
}
```