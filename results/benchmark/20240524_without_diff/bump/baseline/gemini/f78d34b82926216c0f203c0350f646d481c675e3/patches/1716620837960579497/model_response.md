```java
import develop.p2p.lib.*;

public class NPCTeleport {
  public static void main(String[] args) {
    // Create a new P2PClient object.
    P2PClient client = new P2PClient();

    // Connect to the P2P network.
    client.connect("localhost", 12345);

    // Create a new NPC object.
    NPC npc = new NPC("Bob", 100, 100);

    // Teleport the NPC to a new location.
    npc.teleport(200, 200);

    // Disconnect from the P2P network.
    client.disconnect();
  }
}
```