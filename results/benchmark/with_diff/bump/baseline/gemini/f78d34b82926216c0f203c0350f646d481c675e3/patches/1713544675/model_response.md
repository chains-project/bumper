```java
import tokyo.peya.lib.WaveCreator;

public class Decorations {

    public static WaveCreator waveCreator;

    public static void init() {
        waveCreator = new WaveCreator(44100, 2, 16);
    }

    public static void playSound(double frequency, double duration, double volume) {
        waveCreator.get(frequency, true);
    }

}
```