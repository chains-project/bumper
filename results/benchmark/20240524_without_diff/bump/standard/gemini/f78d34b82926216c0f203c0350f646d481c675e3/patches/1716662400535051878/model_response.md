```java
import develop.p2p.lib.*;
import com.google.common.base.Preconditions;

public class NPCTeleport {

    public static void main(String[] args) {
        Preconditions.checkArgument(args.length == 1, "Usage: NPCTeleport <npcId>");
        int npcId = Integer.parseInt(args[0]);

        P2PLib.getInstance().teleportToNPC(npcId);
    }
}
```