```java
import develop.p2p.lib.packet.Packet;

public class NPCTeleport {

    public static void main(String[] args) {
        // Create a new packet with the given ID
        Packet packet = new Packet(1);

        // Set the packet's data
        packet.setData(new byte[]{1, 2, 3, 4});

        // Send the packet
        packet.send();
    }
}
```