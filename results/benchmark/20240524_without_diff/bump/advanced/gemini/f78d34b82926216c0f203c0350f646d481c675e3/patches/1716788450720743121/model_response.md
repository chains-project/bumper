```java
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public static WaveCreator waveCreator;

    public static void init() {
        waveCreator = new WaveCreator();
    }

    public static void createWave(String path, int duration, int volume) {
        waveCreator.createWave(path, duration, volume);
    }
}
```