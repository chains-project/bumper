```java
import develop.p2p.lib.*;
import net.minecraft.server.v1_16_R3.EntityPlayer;
import org.bukkit.craftbukkit.v1_16_R3.entity.CraftPlayer;

public class NPCTeleport {
    public static void teleport(EntityPlayer player, double x, double y, double z) {
        CraftPlayer craftPlayer = (CraftPlayer) player.getBukkitEntity();
        craftPlayer.teleport(craftPlayer.getLocation().add(x, y, z));
    }
}
```