```java
import develop.p2p.lib.WaveCreator;
import develop.p2p.lib.WaveFile;

public class Decorations {

    public static WaveFile createWaveFile(int sampleRate, int numChannels, int bitsPerSample, int duration) {
        WaveCreator waveCreator = new WaveCreator(sampleRate, numChannels, bitsPerSample);
        waveCreator.createWaveFile(duration);
        return waveCreator.getWaveFile();
    }
}
```