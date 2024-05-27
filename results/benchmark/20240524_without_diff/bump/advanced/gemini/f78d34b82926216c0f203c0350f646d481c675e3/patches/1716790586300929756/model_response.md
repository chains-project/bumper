```java
import develop.p2p.lib.*;
import org.bukkit.entity.Player;

public class NPCTeleport {

    public static void teleport(Player player, String server) {
        // Check if the server exists
        if (!ServerManager.getInstance().getServerList().contains(server)) {
            player.sendMessage("§cServer not found.");
            return;
        }

        // Get the server object
        Server targetServer = ServerManager.getInstance().getServer(server);

        // Check if the player is online
        if (targetServer.getPlayer(player.getName()) != null) {
            player.sendMessage("§cPlayer is already online on that server.");
            return;
        }

        // Teleport the player
        player.teleport(targetServer.getSpawnLocation());
        player.sendMessage("§aTeleported to " + server + ".");
    }
}
```