```java
import com.comphenix.protocol.wrappers.WrappedDataWatcher;
import develop.p2p.lib.WaveCreator;
import org.bukkit.Location;
import org.bukkit.entity.Entity;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.util.Vector;

public class Decorations {

    public static void spawnWave(Location location, Vector direction, Player player, int radius) {
        if (player.hasPermission("develop.p2p.wave")) {
            Entity wave = location.getWorld().spawnEntity(location, EntityType.ARMOR_STAND);
            wave.setInvisible(true);
            wave.setGravity(false);
            wave.setSilent(true);
            wave.setInvulnerable(true);
            WrappedDataWatcher watcher = new WrappedDataWatcher(wave);
            watcher.setObject(0, (byte) 32);
            watcher.setObject(17, (byte) 17);
            watcher.setObject(18, (byte) 17);
            watcher.setObject(19, (byte) 17);
            watcher.setObject(20, (byte) 17);
            watcher.setObject(21, (byte) 17);
            watcher.setObject(22, (byte) 17);
            watcher.setObject(23, (byte) 17);
            watcher.setObject(24, (byte) 17);
            wave.setCustomName(player.getName() + "'s Wave");
            wave.setCustomNameVisible(true);
            WaveCreator waveCreator = new WaveCreator(wave, direction, radius);
            waveCreator.start();
        }
    }
}
```