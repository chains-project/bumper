```java
import develop.p2p.lib.WaveCreator;
import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import org.bukkit.Location;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class Decorations extends JavaPlugin implements Listener {
    private WaveCreator waveCreator;

    public Decorations() {
        this.waveCreator = new WaveCreator(Paths.get(File.separator + "home" + File.separator + "pey" + File.separator + "Documents" + File.separator + "PeyangSuperbAntiCheat" + File.separator + "sound" + File.separator + "decoration"), 16000);
    }

    public void onEnable() {
        this.getServer().getPluginManager().registerEvents(this, this);
    }

    @EventHandler
    public void onJoin(PlayerJoinEvent event) {
        Player player = event.getPlayer();
        Location location = player.getLocation();
        this.waveCreator.play("decoration.wav", location, 1.0F, 1.0F);
    }
}
```