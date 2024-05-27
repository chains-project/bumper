```java
import develop.p2p.lib.*;
import develop.p2p.lib.message.Message;
import develop.p2p.lib.message.MessageListener;
import develop.p2p.lib.node.Node;
import develop.p2p.lib.node.NodeAddress;

public class NPCTeleport {

    private final Node node;

    public NPCTeleport(Node node) {
        this.node = node;
        this.node.addMessageListener(new MessageListener() {
            @Override
            public void onMessage(NodeAddress sender, Message message) {
                if (message.getType() == Message.Type.NPC_TELEPORT) {
                    // Handle NPC teleport message
                }
            }
        });
    }

    public void teleportNPC(int npcId, NodeAddress targetNode) {
        // Send NPC teleport message
        Message message = new Message(Message.Type.NPC_TELEPORT);
        message.putInt("npcId", npcId);
        message.putNodeAddress("targetNode", targetNode);
        node.sendMessage(targetNode, message);
    }
}
```