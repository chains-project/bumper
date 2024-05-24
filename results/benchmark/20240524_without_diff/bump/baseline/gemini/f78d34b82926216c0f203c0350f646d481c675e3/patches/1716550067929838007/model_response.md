```java
import tokyo.peya.lib.*;

public class NPCTeleport {
    public static void main(String[] args) {
        FileConfiguration config = new FileConfiguration("config.yml");
        config.load();

        // Get the NPC teleport location from the config file
        String location = config.getString("npc-teleport.location");

        // Check if the location is valid
        if (location == null || location.isEmpty()) {
            System.out.println("Invalid NPC teleport location in config file.");
            return;
        }

        // Teleport the player to the specified location
        // ...
    }
}
```