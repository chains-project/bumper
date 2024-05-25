```java
import com.google.common.collect.ImmutableList;
import develop.p2p.lib.WaveCreator;
import develop.p2p.lib.WaveCreator.WaveGenerator;
import develop.p2p.lib.WaveCreator.WaveGenerator.WaveGeneratorConfig;
import develop.p2p.lib.WaveCreator.WaveGenerator.WaveGeneratorConfig.WaveGeneratorConfigBuilder;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import org.bukkit.Location;
import org.bukkit.entity.Player;

public class Decorations {

    public static void spawnWave(Player player, Location location, Function<WaveGeneratorConfigBuilder, WaveGeneratorConfig> configBuilder) {
        List<WaveGeneratorConfig> configs = new ArrayList<>();
        configs.add(configBuilder.apply(WaveGeneratorConfig.newBuilder()));
        WaveCreator.spawnWave(player, location, ImmutableList.copyOf(configs));
    }
}
```