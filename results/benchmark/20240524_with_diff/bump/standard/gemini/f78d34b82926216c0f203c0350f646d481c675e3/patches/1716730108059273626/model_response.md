```java
import tokyo.peya.lib.*;

public class NPCTeleport {

    public static void onTeleport(final Player player, final Location location) {
        if (player == null || location == null) {
            return;
        }
        final FileConfiguration config = FileConfiguration.getInstance();
        final String worldName = location.getWorld().getName();
        final double x = location.getX();
        final double y = location.getY();
        final double z = location.getZ();
        final double yaw = location.getYaw();
        final double pitch = location.getPitch();
        final String message = config.getString("teleport.message");
        if (message != null) {
            player.sendMessage(message.replace("%world%", worldName).replace("%x%", String.valueOf(x)).replace("%y%", String.valueOf(y)).replace("%z%", String.valueOf(z)).replace("%yaw%", String.valueOf(yaw)).replace("%pitch%", String.valueOf(pitch)));
        }
        player.teleport(location);
    }
}
```