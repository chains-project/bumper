Here's a proposed patch for the code:
```java
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Particle;
import org.bukkit.util.Vector;

import java.util.Random;

public class Decorations {
    // ...

    public static void magic(Player player, int seconds) {
        final int[] count = {0};
        WaveCreator wave = new WaveCreator(0.8, 1.8, 0.1);

        Bukkit.getScheduler().runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), () -> {
            Location center = player.getLocation();

            circle(center, count, 3, Particle.CRIT);

            circle(center.add(0, 0.7, 0), count, 2.7, Particle.ENCHANTMENT_TABLE);

            circle(center.clone().add(0, wave.get(0.01, false), 0), count, wave.getStatic());

            circle(center.clone().add(3.2, 0.7, 3.2), count, 1.5);
            circle(center.clone().add(-3.2, 0.7, -3.2), count, 1.5);
            circle(center.clone().add(-3.2, 0.7, 3.2), count, 1.5);
            circle(center.clone().add(3.2, 0.7, -3.2), count, 1.5);

            circle(center.clone().add(0, 1.5, 0), count, 5, Particle.SPELL_WITCH);

            count[0]++;

            Location loc1 = center.clone().add(3, 0.7, 0);
            Location loc2 = center.clone().add(-1.5, 0.7, 2.3);
            Location loc3 = center.clone().add(-1.5, 0.7, -2.3);
            Location loc4 = center.clone().add(-3, 0.7, 0);

            line(loc1, loc2);
            line(loc2, loc3);
            line(loc3, loc4);
            line(loc4, loc1);

            line(loc4.clone().add(0, 0, 4.6), loc2.clone().add(0, 0, -4.6));
            line(loc2.clone().add(0, 0, -4.6), loc3.clone().add(3, 0, -4.6));
            line(loc3.clone().add(3, 0, -4.6), loc1);

            line(loc1.clone().add(6, 0, 0), loc4.clone().add(0, 0, 6));
        }, 0L, 1L);

        Bukkit.getScheduler().runTaskLater(PeyangSuperbAntiCheat.getPlugin(), () -> {
            Bukkit.getScheduler().cancelTasks(PeyangSuperbAntiCheat.getPlugin(), task -> true);
        }, seconds * 20L);
    }

    private static void circle(Location center, int[] count, double radius, double yOffset, Particle particle) {
        circle(center, count, radius, yOffset, particle, 32);
    }

    private static void circle(Location center, int[] count, double radius, double yOffset, Particle particle, int particles) {
        Random random = new Random();
        for (double i = 0; i < Math.PI * 2; i++) {
            double x = radius * Math.cos(i) + center.getX();
            double z = radius * Math.sin(i) + center.getZ();
            center.getWorld().spawnParticle(particle, x, center.getY() + yOffset, z, 1, new Particle.DustOptions(new Color(random.nextFloat(), random.nextFloat(), random.nextFloat()), 1));
            count[0]++;
        }
    }

    private static void line(Location start, Location end) {
        Vector direction = end.toVector().subtract(start.toVector()).normalize();
        double distance = start.distance(end);

        for (double i = 0; i <= distance; i += 0.1) {
            Location loc = start.clone().add(direction.multiply(i));
            loc.getWorld().spawnParticle(Particle.REDSTONE, loc, 1, new Particle.DustOptions(new Color(0, 0, 0), 1));
        }
    }
}
```
The main change I made was to replace the `BukkitRunnable` class with the `BukkitScheduler` class, which is a better way to handle tasks in Bukkit. I also simplified the `circle` and `line` methods by removing unnecessary cloning and adding.

Note: The `WaveCreator` class was not provided in the code snippet, so I assumed it was a custom class that was not causing the issue. If this is not the case, please provide the implementation of the `WaveCreator` class.

Also, note that the `line` method was changed to use a different way of drawing a line using particles, since the previous implementation was not provided. You may need to adjust this method to fit your specific needs.