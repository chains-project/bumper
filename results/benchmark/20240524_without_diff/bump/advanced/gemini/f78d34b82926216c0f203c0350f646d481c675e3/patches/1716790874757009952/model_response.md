```java
import develop.p2p.lib.*;

public class NPCTeleport {

    public void onEnable() {
        // Get the instance of the P2PLib class
        P2PLib p2pLib = P2PLib.getInstance();

        // Register the listener for the NPC_TELEPORT event
        p2pLib.registerListener(new NPC_TELEPORTListener() {
            @Override
            public void onNPC_TELEPORT(NPC_TELEPORTEvent event) {
                // Get the NPC that teleported
                NPC npc = event.getNPC();

                // Get the location the NPC teleported to
                Location location = event.getLocation();

                // Print the NPC's name and the location it teleported to
                System.out.println("NPC " + npc.getName() + " teleported to " + location.toString());
            }
        });
    }
}
```