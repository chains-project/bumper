```java
import java.util.ArrayList;
import java.util.List;

import develop.p2p.lib.*;

public class NPCTeleport {

    private final NPCTeleportListener listener;

    public NPCTeleport(NPCTeleportListener listener) {
        this.listener = listener;
    }

    public void onNPCTeleport(String npcName, String playerName, String worldName, double x, double y, double z) {
        List<String> messages = new ArrayList<>();
        messages.add("NPC " + npcName + " teleported player " + playerName + " to world " + worldName + " at coordinates (" + x + ", " + y + ", " + z + ").");
        listener.onNPCTeleport(messages);
    }
}
```