```java
import net.minecraft.server.v1_19_R1.World;
import org.bukkit.craftbukkit.v1_19_R1.CraftWorld;
import org.bukkit.entity.Player;

public class Decorations {

    public static void playSound(Player player, String soundName, float volume, float pitch) {
        World world = ((CraftWorld) player.getWorld()).getHandle();
        world.playSound(player.getLocation(), soundName, volume, pitch);
    }
}
```