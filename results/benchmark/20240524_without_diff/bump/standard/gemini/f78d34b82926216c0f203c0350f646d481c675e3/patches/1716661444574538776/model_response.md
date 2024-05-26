```java
import develop.p2p.lib.WaveCreator;
import java.util.ArrayList;
import java.util.List;

public class Decorations {

    private final WaveCreator waveCreator;

    public Decorations(WaveCreator waveCreator) {
        this.waveCreator = waveCreator;
    }

    public List<String> getDecorations() {
        List<String> decorations = new ArrayList<>();
        decorations.add("WaveCreator: " + waveCreator.getName());
        return decorations;
    }
}
```