```java
import develop.p2p.lib.WaveCreator;
import org.spongepowered.api.Sponge;

public class Decorations {

    public static void main(String[] args) {
        WaveCreator waveCreator = Sponge.getServiceManager().provideUnchecked(WaveCreator.class);
        waveCreator.createWave();
    }
}
```