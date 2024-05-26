```java
import develop.p2p.lib.WaveCreator;
import develop.p2p.lib.WaveCreatorFactory;

public class Decorations {

    public static WaveCreator createWaveCreator(int sampleRate, int channels, int bitsPerSample) {
        return WaveCreatorFactory.createWaveCreator(sampleRate, channels, bitsPerSample);
    }

}
```