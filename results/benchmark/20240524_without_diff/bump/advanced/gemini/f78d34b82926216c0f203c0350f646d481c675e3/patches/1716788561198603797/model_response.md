```java
import net.minecraft.server.v1_12_R1.PacketPlayOutEntityDestroy;

public class Decorations {
    public static void sendDestroy(Player player, Entity entity) {
        PacketPlayOutEntityDestroy packet = new PacketPlayOutEntityDestroy(entity.getId());
        player.playerConnection.sendPacket(packet);
    }
}
```