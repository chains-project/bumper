```java
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public void createWave(String name, String path, String type) {
        WaveCreator waveCreator = new WaveCreator(name, path, type);
        waveCreator.create();
    }
}
```