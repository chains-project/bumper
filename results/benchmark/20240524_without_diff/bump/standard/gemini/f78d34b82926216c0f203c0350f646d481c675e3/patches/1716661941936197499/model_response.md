```java
import net.minecraft.server.v1_16_R3.PacketPlayOutEntityDestroy;
import org.bukkit.craftbukkit.v1_16_R3.entity.CraftPlayer;
import org.bukkit.entity.Player;

import java.util.List;

public class Decorations {
    public static void sendDestroyPacket(Player player, List<Integer> entityIds) {
        PacketPlayOutEntityDestroy packet = new PacketPlayOutEntityDestroy(entityIds.stream().mapToInt(Integer::intValue).toArray());
        ((CraftPlayer) player).getHandle().playerConnection.sendPacket(packet);
    }
}
```