```java
import develop.p2p.lib.*;

public class NPCTeleport {

    public static void main(String[] args) {
        // Create a new NetworkManager instance.
        NetworkManager networkManager = new NetworkManager();

        // Create a new Client instance.
        Client client = new Client(networkManager);

        // Connect to the server.
        client.connect("localhost", 8080);

        // Send a message to the server.
        client.sendMessage("Hello, world!");

        // Close the connection.
        client.close();
    }
}
```