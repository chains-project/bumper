```java
import develop.p2p.lib.*;
import net.md_5.bungee.api.chat.TextComponent;
import org.bukkit.entity.Player;

import java.util.Collection;

public class NPCTeleport {

    private final String npcName;

    public NPCTeleport(String npcName) {
        this.npcName = npcName;
    }

    public void teleport(Player player) {
        Collection<Player> players = player.getWorld().getPlayers();

        for (Player p : players) {
            if (p.getName().equalsIgnoreCase(npcName)) {
                player.teleport(p.getLocation());
                player.spigot().sendMessage(TextComponent.fromLegacyText("Teleported to NPC " + npcName));
                return;
            }
        }

        player.spigot().sendMessage(TextComponent.fromLegacyText("NPC " + npcName + " not found"));
    }
}
```