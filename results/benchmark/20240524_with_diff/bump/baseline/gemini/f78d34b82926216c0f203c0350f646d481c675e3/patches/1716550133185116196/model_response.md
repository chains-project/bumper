```java
import tokyo.peya.lib.WaveCreator;

public class Decorations {
    public static void main(String[] args) {
        WaveCreator waveCreator = new WaveCreator(1.0, 2.0, 3.0);
        double value = waveCreator.get(0.5, true);
        System.out.println(value);
    }
}
```