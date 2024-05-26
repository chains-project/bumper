```java
import ml.peya.plugins.Objects.Decorations;
import net.minecraft.entity.player.EntityPlayerMP;
import net.minecraft.server.MinecraftServer;
import net.minecraft.world.World;

import java.util.ArrayList;
import java.util.List;

public class WaveCreator {

    private static final List<EntityPlayerMP> players = new ArrayList<>();

    public static void createWave(World world, int x, int y, int z, int radius, int height, int delay) {
        MinecraftServer server = MinecraftServer.getServer();
        for (EntityPlayerMP player : server.getPlayerList().getPlayers()) {
            if (player.getDistanceSq(x, y, z) <= radius * radius) {
                players.add(player);
            }
        }

        new Thread(() -> {
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            for (EntityPlayerMP player : players) {
                player.setPositionAndUpdate(x, y + height, z);
            }
        }).start();
    }
}
```