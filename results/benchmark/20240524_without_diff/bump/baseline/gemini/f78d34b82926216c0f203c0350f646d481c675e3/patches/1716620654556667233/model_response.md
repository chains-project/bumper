```java
  import develop.p2p.lib.*;

  import java.util.ArrayList;
  import java.util.List;

  public class NPCTeleport {

    public static List<String> getPlayers(String world) {
      List<String> players = new ArrayList<>();
      for (Player player : Bukkit.getOnlinePlayers()) {
        if (player.getWorld().getName().equalsIgnoreCase(world)) {
          players.add(player.getName());
        }
      }
      return players;
    }

    public static void teleport(String player, String world) {
      Player p = Bukkit.getPlayer(player);
      if (p != null) {
        p.teleport(Bukkit.getWorld(world).getSpawnLocation());
      }
    }

    public static void main(String[] args) {
      String world = "world";
      List<String> players = getPlayers(world);
      for (String player : players) {
        teleport(player, world);
      }
    }
  }
```