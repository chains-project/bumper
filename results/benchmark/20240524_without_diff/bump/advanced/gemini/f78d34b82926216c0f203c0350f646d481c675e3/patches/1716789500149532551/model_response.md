```java
import develop.p2p.lib.*;

public class NPCTeleport {

    public static void main(String[] args) {
        // Create a new P2PClient instance
        P2PClient client = new P2PClient();

        // Connect to the server
        client.connect("localhost", 12345);

        // Send a message to the server
        client.send("Hello, world!");

        // Close the connection
        client.close();
    }
}
```