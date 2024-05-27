```java
import develop.p2p.lib.*;

public class NPCTeleport {

    public void onEnable() {
        // Get the server instance
        Server server = Server.getInstance();

        // Register the event listener
        server.getPluginManager().registerEvents(new NPCTeleportListener(), this);

        // Register the command
        server.getCommand("npcteleport").setExecutor(new NPCTeleportCommand());

        // Load the configuration
        ConfigManager.loadConfig("npcteleport.yml");

        // Create the teleport manager
        TeleportManager teleportManager = new TeleportManager();

        // Create the NPC manager
        NPCManager npcManager = new NPCManager();

        // Create the command manager
        CommandManager commandManager = new CommandManager();

        // Create the listener manager
        ListenerManager listenerManager = new ListenerManager();

        // Register the managers
        server.getPluginManager().registerEvents(listenerManager, this);
        server.getCommand("npcteleport").setExecutor(commandManager);

        // Load the NPCs
        npcManager.loadNPCs();

        // Start the teleport manager
        teleportManager.start();
    }
}
```