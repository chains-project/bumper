```java
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public void createWave() {
        // Create a wave file
        WaveCreator waveCreator = new WaveCreator(44100, 16, 1); // 44100 Hz, 16 bits per sample, 1 channel
        waveCreator.addSineWave(440, 1.0, 0, 1000); // Add a sine wave at 440 Hz for 1 second
        waveCreator.writeToFile("wave.wav"); // Write the wave file to disk
    }
}
```