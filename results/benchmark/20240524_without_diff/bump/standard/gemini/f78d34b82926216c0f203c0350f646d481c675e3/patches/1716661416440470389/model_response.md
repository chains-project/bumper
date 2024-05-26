```java
import org.bukkit.entity.Player;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerMoveEvent;
import org.bukkit.event.player.PlayerToggleFlightEvent;
import org.bukkit.plugin.Plugin;

public class Decorations implements Listener {

    private final Plugin plugin;

    public Decorations(Plugin plugin) {
        this.plugin = plugin;
        plugin.getServer().getPluginManager().registerEvents(this, plugin);
    }

    @EventHandler
    public void onPlayerMove(PlayerMoveEvent event) {
        Player player = event.getPlayer();
        if (player.isFlying() && player.getLocation().getY() > 250) {
            player.setFlying(false);
            player.sendMessage("You cannot fly above 250 blocks.");
        }
    }

    @EventHandler
    public void onPlayerToggleFlight(PlayerToggleFlightEvent event) {
        Player player = event.getPlayer();
        if (player.getLocation().getY() > 250) {
            event.setCancelled(true);
            player.sendMessage("You cannot fly above 250 blocks.");
        }
    }
}
```