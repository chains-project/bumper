```java
import develop.p2p.lib.Peer;

public class NPCTeleport {

    private Peer peer;

    public NPCTeleport(Peer peer) {
        this.peer = peer;
    }

    public void onNPCTeleport(int npcId, int x, int y, int z) {
        peer.sendPacket(new NPCTeleportPacket(npcId, x, y, z));
    }

    private static class NPCTeleportPacket {

        private final int npcId;
        private final int x;
        private final int y;
        private final int z;

        public NPCTeleportPacket(int npcId, int x, int y, int z) {
            this.npcId = npcId;
            this.x = x;
            this.y = y;
            this.z = z;
        }

        // ++ Getters and setters for npcId, x, y, and z
    }
}
```