```java
import tokyo.peya.lib.*;

public class NPCTeleport {
    public static void main(String[] args) {
        FileConfiguration config = new FileConfiguration("config.yml");
        config.load();
        
        String npcName = config.getString("npcName");
        double x = config.getDouble("x");
        double y = config.getDouble("y");
        double z = config.getDouble("z");
        
        // Create a new WaveCreator object
        WaveCreator waveCreator = new WaveCreator(x, y, z);
        
        // Get the wave value at a specific time
        double waveValue = waveCreator.get(0.5, true);
        
        // Print the wave value
        System.out.println("Wave value: " + waveValue);
    }
}
```