```java
import tokyo.peya.lib.*;

public class NPCTeleport {

    public NPCTeleport() {
    }

    public void onEnable() {
        FileConfiguration config = new FileConfiguration("plugins/NPCTeleport/config.yml");
        config.load();

        String worldName = config.getString("world");
        double x = config.getDouble("x");
        double y = config.getDouble("y");
        double z = config.getDouble("z");
        double yaw = config.getDouble("yaw");
        double pitch = config.getDouble("pitch");

        // Create the WaveCreator object
        WaveCreator waveCreator = new WaveCreator(x, y, z);

        // Get the wave value at the current time
        double waveValue = waveCreator.get(System.currentTimeMillis(), false);

        // Calculate the new Y coordinate based on the wave value
        double newY = y + waveValue;

        // Set the new Y coordinate for the NPC
        // ...
    }
}
```