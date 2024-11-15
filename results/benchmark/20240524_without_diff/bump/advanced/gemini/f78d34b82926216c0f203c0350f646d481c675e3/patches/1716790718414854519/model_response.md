```java
import develop.p2p.lib.*;
import develop.p2p.lib.msg.Message;
import develop.p2p.lib.msg.MessageListener;
import develop.p2p.lib.node.Node;
import develop.p2p.lib.node.NodeBuilder;
import develop.p2p.lib.node.NodeConfiguration;
import develop.p2p.lib.node.NodeStatusListener;
import develop.p2p.lib.util.Address;
import develop.p2p.lib.util.Network;
import develop.p2p.lib.util.Random;
import develop.p2p.lib.util.Timer;
import develop.p2p.lib.util.concurrent.Future;
import develop.p2p.lib.util.concurrent.FutureListener;
import develop.p2p.lib.util.concurrent.Promise;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import ml.peya.plugins.Detect.NPCTeleport;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.entity.Player;
import org.bukkit.plugin.Plugin;
import org.bukkit.scheduler.BukkitRunnable;

public class NPCTeleport
{
    private static final int PORT = 12345;
    private static final String HOST = "localhost";
    private static final int TIMEOUT = 5000;
    private static final String KEY = "YOUR_KEY";
    private static final int MAX_NODES = 10;
    private static final int MIN_NODES = 5;
    private static final int MAX_RETRIES = 3;
    private static final int RETRY_DELAY = 1000;
    private static final int MESSAGE_TIMEOUT = 1000;
    private static Plugin plugin;
    private static Node node;
    private static Map<String, Location> teleportLocations = new HashMap<>();

    public NPCTeleport(Plugin plugin)
    {
        NPCTeleport.plugin = plugin;
        startNode();
    }

    private void startNode()
    {
        NodeConfiguration configuration = new NodeConfiguration();
        configuration.setPort(PORT);
        configuration.setHost(HOST);
        configuration.setTimeout(TIMEOUT);
        configuration.setKey(KEY);
        configuration.setMaxNodes(MAX_NODES);
        configuration.setMinNodes(MIN_NODES);
        configuration.setMaxRetries(MAX_RETRIES);
        configuration.setRetryDelay(RETRY_DELAY);
        configuration.setMessageTimeout(MESSAGE_TIMEOUT);
        node = new NodeBuilder().withConfiguration(configuration).build();
        node.addNodeStatusListener(new NodeStatusListener()
        {
            public void onNodeAdded(Node node)
            {
                System.out.println("Node added: " + node.getAddress());
            }

            public void onNodeRemoved(Node node)
            {
                System.out.println("Node removed: " + node.getAddress());
            }
        });
        node.addMessageListener(new MessageListener()
        {
            public void onMessageReceived(Node node, Message message)
            {
                if (message.getType().equals("TELEPORT"))
                {
                    String playerName = message.getData("player");
                    String locationName = message.getData("location");
                    Location location = teleportLocations.get(locationName);
                    if (location != null)
                    {
                        Player player = Bukkit.getPlayer(playerName);
                        if (player != null)
                        {
                            player.teleport(location);
                        }
                    }
                }
            }
        });
        node.start();
    }

    public void addTeleportLocation(String name, Location location)
    {
        teleportLocations.put(name, location);
    }

    public void teleportPlayer(Player player, String locationName)
    {
        Location location = teleportLocations.get(locationName);
        if (location != null)
        {
            Message message = new Message("TELEPORT");
            message.setData("player", player.getName());
            message.setData("location", locationName);
            node.sendMessage(message);
        }
    }
}
```