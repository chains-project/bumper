```java
import com.google.common.collect.ImmutableList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;
import java.util.stream.Collectors;
import org.bukkit.Bukkit;
import org.bukkit.Chunk;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.entity.Player;
import org.bukkit.scheduler.BukkitRunnable;
import org.bukkit.util.Vector;

public class Decorations {

    private final List<Location> locations;
    private final ConcurrentMap<Location, Block> blocks;

    public Decorations(List<Location> locations) {
        this.locations = ImmutableList.copyOf(locations);
        this.blocks = new ConcurrentHashMap<>();
    }

    public void spawn(Player player) {
        for (Location location : locations) {
            if (isFarFromPlayer(location, player)) {
                continue;
            }

            Block block = location.getBlock();
            blocks.put(location, block);
            block.setType(Material.BEDROCK);
        }
    }

    public void despawn(Player player) {
        for (Location location : locations) {
            if (isFarFromPlayer(location, player)) {
                continue;
            }

            Block block = blocks.remove(location);
            if (block != null) {
                block.setType(Material.AIR);
            }
        }
    }

    private boolean isFarFromPlayer(Location location, Player player) {
        return location.getWorld() != player.getWorld() || location.distanceSquared(player.getLocation()) > 10000;
    }

    public static Decorations create(List<Location> locations) {
        return new Decorations(locations);
    }

    public void update(Consumer<Location> consumer) {
        for (Location location : locations) {
            consumer.accept(location);
        }
    }

    public void updateAsync(Consumer<Location> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    consumer.accept(location);
                }
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateAsync(Consumer<Location> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    consumer.accept(location);
                }
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateSync(Consumer<Location> consumer) {
        for (Location location : locations) {
            consumer.accept(location);
        }
    }

    public void updateSync(Consumer<Location> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    consumer.accept(location);
                }
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateChunks(Consumer<Chunk> consumer) {
        Map<World, List<Location>> worldLocations = locations.stream()
                .collect(Collectors.groupingBy(Location::getWorld));

        for (Map.Entry<World, List<Location>> entry : worldLocations.entrySet()) {
            World world = entry.getKey();
            List<Location> worldLocationsList = entry.getValue();

            for (int x = (int) Math.floor(worldLocationsList.stream().mapToDouble(Location::getX).min().orElse(0)) >> 4;
                 x <= (int) Math.ceil(worldLocationsList.stream().mapToDouble(Location::getX).max().orElse(0)) >> 4;
                 x++) {
                for (int z = (int) Math.floor(worldLocationsList.stream().mapToDouble(Location::getZ).min().orElse(0)) >> 4;
                     z <= (int) Math.ceil(worldLocationsList.stream().mapToDouble(Location::getZ).max().orElse(0)) >> 4;
                     z++) {
                    Chunk chunk = world.getChunkAt(x, z);
                    consumer.accept(chunk);
                }
            }
        }
    }

    public void updateChunksAsync(Consumer<Chunk> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                updateChunks(consumer);
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateChunksAsync(Consumer<Chunk> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                updateChunks(consumer);
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateChunksSync(Consumer<Chunk> consumer) {
        updateChunks(consumer);
    }

    public void updateChunksSync(Consumer<Chunk> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                updateChunks(consumer);
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateBlocks(Consumer<Block> consumer) {
        for (Location location : locations) {
            Block block = location.getBlock();
            consumer.accept(block);
        }
    }

    public void updateBlocksAsync(Consumer<Block> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    Block block = location.getBlock();
                    consumer.accept(block);
                }
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateBlocksAsync(Consumer<Block> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    Block block = location.getBlock();
                    consumer.accept(block);
                }
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateBlocksSync(Consumer<Block> consumer) {
        for (Location location : locations) {
            Block block = location.getBlock();
            consumer.accept(block);
        }
    }

    public void updateBlocksSync(Consumer<Block> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    Block block = location.getBlock();
                    consumer.accept(block);
                }
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateEntities(Consumer<Player> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            for (Player player : world.getPlayers()) {
                if (isFarFromPlayer(location, player)) {
                    continue;
                }

                consumer.accept(player);
            }
        }
    }

    public void updateEntitiesAsync(Consumer<Player> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (Player player : world.getPlayers()) {
                        if (isFarFromPlayer(location, player)) {
                            continue;
                        }

                        consumer.accept(player);
                    }
                }
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateEntitiesAsync(Consumer<Player> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (Player player : world.getPlayers()) {
                        if (isFarFromPlayer(location, player)) {
                            continue;
                        }

                        consumer.accept(player);
                    }
                }
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateEntitiesSync(Consumer<Player> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            for (Player player : world.getPlayers()) {
                if (isFarFromPlayer(location, player)) {
                    continue;
                }

                consumer.accept(player);
            }
        }
    }

    public void updateEntitiesSync(Consumer<Player> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (Player player : world.getPlayers()) {
                        if (isFarFromPlayer(location, player)) {
                            continue;
                        }

                        consumer.accept(player);
                    }
                }
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateRays(Consumer<Vector> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            Vector direction = location.getDirection();
            for (int i = 0; i < 100; i++) {
                location.add(direction);
                Block block = location.getBlock();
                if (block.getType() != Material.AIR) {
                    break;
                }

                consumer.accept(location.toVector());
            }
        }
    }

    public void updateRaysAsync(Consumer<Vector> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    Vector direction = location.getDirection();
                    for (int i = 0; i < 100; i++) {
                        location.add(direction);
                        Block block = location.getBlock();
                        if (block.getType() != Material.AIR) {
                            break;
                        }

                        consumer.accept(location.toVector());
                    }
                }
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateRaysAsync(Consumer<Vector> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    Vector direction = location.getDirection();
                    for (int i = 0; i < 100; i++) {
                        location.add(direction);
                        Block block = location.getBlock();
                        if (block.getType() != Material.AIR) {
                            break;
                        }

                        consumer.accept(location.toVector());
                    }
                }
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateRaysSync(Consumer<Vector> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            Vector direction = location.getDirection();
            for (int i = 0; i < 100; i++) {
                location.add(direction);
                Block block = location.getBlock();
                if (block.getType() != Material.AIR) {
                    break;
                }

                consumer.accept(location.toVector());
            }
        }
    }

    public void updateRaysSync(Consumer<Vector> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    Vector direction = location.getDirection();
                    for (int i = 0; i < 100; i++) {
                        location.add(direction);
                        Block block = location.getBlock();
                        if (block.getType() != Material.AIR) {
                            break;
                        }

                        consumer.accept(location.toVector());
                    }
                }
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateSpheres(Consumer<Location> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            for (int x = -5; x <= 5; x++) {
                for (int y = -5; y <= 5; y++) {
                    for (int z = -5; z <= 5; z++) {
                        Location sphereLocation = location.clone().add(x, y, z);
                        if (sphereLocation.distanceSquared(location) <= 25) {
                            consumer.accept(sphereLocation);
                        }
                    }
                }
            }
        }
    }

    public void updateSpheresAsync(Consumer<Location> consumer) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (int x = -5; x <= 5; x++) {
                        for (int y = -5; y <= 5; y++) {
                            for (int z = -5; z <= 5; z++) {
                                Location sphereLocation = location.clone().add(x, y, z);
                                if (sphereLocation.distanceSquared(location) <= 25) {
                                    consumer.accept(sphereLocation);
                                }
                            }
                        }
                    }
                }
            }
        }.runTaskAsynchronously(WaveCreator.getPlugin());
    }

    public void updateSpheresAsync(Consumer<Location> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (int x = -5; x <= 5; x++) {
                        for (int y = -5; y <= 5; y++) {
                            for (int z = -5; z <= 5; z++) {
                                Location sphereLocation = location.clone().add(x, y, z);
                                if (sphereLocation.distanceSquared(location) <= 25) {
                                    consumer.accept(sphereLocation);
                                }
                            }
                        }
                    }
                }
            }
        }.runTaskLaterAsynchronously(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }

    public void updateSpheresSync(Consumer<Location> consumer) {
        for (Location location : locations) {
            World world = location.getWorld();
            if (world == null) {
                continue;
            }

            for (int x = -5; x <= 5; x++) {
                for (int y = -5; y <= 5; y++) {
                    for (int z = -5; z <= 5; z++) {
                        Location sphereLocation = location.clone().add(x, y, z);
                        if (sphereLocation.distanceSquared(location) <= 25) {
                            consumer.accept(sphereLocation);
                        }
                    }
                }
            }
        }
    }

    public void updateSpheresSync(Consumer<Location> consumer, long delay, TimeUnit timeUnit) {
        new BukkitRunnable() {
            @Override
            public void run() {
                for (Location location : locations) {
                    World world = location.getWorld();
                    if (world == null) {
                        continue;
                    }

                    for (int x = -5; x <= 5; x++) {
                        for (int y = -5; y <= 5; y++) {
                            for (int z = -5; z <= 5; z++) {
                                Location sphereLocation = location.clone().add(x, y, z);
                                if (sphereLocation.distanceSquared(location) <= 25) {
                                    consumer.accept(sphereLocation);
                                }
                            }
                        }
                    }
                }
            }
        }.runTaskLater(WaveCreator.getPlugin(), timeUnit.toMillis(delay));
    }
}
```