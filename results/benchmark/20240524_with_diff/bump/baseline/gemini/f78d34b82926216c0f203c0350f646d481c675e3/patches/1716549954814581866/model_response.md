```java
import tokyo.peya.lib.WaveCreator;

public class Decorations {

    public WaveCreator waveCreator;

    public Decorations() {
        this.waveCreator = new WaveCreator(44100.0, 1.0, 0.0);
    }

    public void playSound(String soundName) {
        // TODO: Implement sound playback using WaveCreator
    }
}
```