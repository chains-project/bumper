```java
import com.mojang.authlib.GameProfile;
import develop.p2p.lib.Protocol;
import net.minecraft.entity.player.EntityPlayerMP;
import net.minecraft.server.management.PlayerList;
import net.minecraft.util.math.BlockPos;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.fml.common.gameevent.TickEvent;

import java.util.UUID;

public class NPCTeleport {
    private static Protocol protocol;

    public NPCTeleport(Protocol protocol) {
        this.protocol = protocol;
    }

    @SubscribeEvent
    public void onPlayerTick(TickEvent.PlayerTickEvent event) {
        if (event.player instanceof EntityPlayerMP) {
            EntityPlayerMP player = (EntityPlayerMP) event.player;
            PlayerList playerList = player.getServer().getPlayerList();
            GameProfile gameProfile = new GameProfile(UUID.fromString("00000000-0000-0000-0000-000000000000"), "NPC");
            EntityPlayerMP npc = new EntityPlayerMP(player.getServer(), player.getServer().getWorld(0), gameProfile, new PlayerList(player.getServer()));
            npc.setPositionAndUpdate(new BlockPos(100, 100, 100));
            playerList.addPlayerToLimbo(npc);
            playerList.sendPacketToAllPlayers(protocol.createSpawnPlayerPacket(npc));
        }
    }
}
```