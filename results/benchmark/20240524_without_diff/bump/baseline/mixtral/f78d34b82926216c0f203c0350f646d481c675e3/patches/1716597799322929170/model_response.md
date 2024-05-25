Here's a possible patch for the failing code:
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
            double i = 0;
            while (i < Math.PI * 2) {
                Location center = player.getLocation();

                circle(center.clone().add(0, 0.9, 0), count[0], 3, Particle.CRIT);

                circle(center.add(0, 0.7, 0), count[0], 2.7, Particle.ENCHANTMENT_TABLE);

                circle(center.clone().add(0, wave.get(0.01, false), 0), count[0], wave.getStatic());

                circle(center.clone().add(3.2, 0.7, 3.2), count[0], 1.5);
                circle(center.clone().add(-3.2, 0.7, -3.2), count[0], 1.5);
                circle(center.clone().add(-3.2, 0.7, 3.2), count[0], 1.5);
                circle(center.clone().add(3.2, 0.7, -3.2), count[0], 1.5);

                circle(center.clone().add(0, 1.5, 0), count[0], 5, Particle.SPELL_WITCH);

                count[0]++;

                i += 0.1;
            }

            Location center = player.getLocation();

            Vector direction1 = new Vector(3, 0.7, 0).subtract(center.toVector()).normalize();
            Vector direction2 = new Vector(-1.5, 0.7, 2.3).subtract(center.toVector()).normalize();
            Vector direction3 = new Vector(-1.5, 0.7, -2.3).subtract(center.toVector()).normalize();

            line(center.clone().add(3, 0.7, 0), center.clone().add(direction1.multiply(3)));
            line(center.clone().add(direction1.multiply(3)), center.clone().add(direction2.multiply(1.5)));
            line(center.clone().add(direction2.multiply(1.5)), center.clone().add(direction3.multiply(1.5)));

            Vector direction4 = new Vector(-3, 0.7, 0).subtract(center.toVector()).normalize();
            Vector direction5 = new Vector(1.5, 0.7, -2.3).subtract(center.toVector()).normalize();
            Vector direction6 = new Vector(1.5, 0.7, 2.3).subtract(center.toVector()).normalize();

            line(center.clone().add(direction4.multiply(3)), center.clone().add(direction5.multiply(1.5)));
            line(center.clone().add(direction5.multiply(1.5)), center.clone().add(direction6.multiply(1.5)));
            line(center.clone().add(direction6.multiply(1.5)), center.clone().add(direction4.multiply(3)));
        }, 0L, 1L);

        Bukkit.getScheduler().runTaskLater(PeyangSuperbAntiCheat.getPlugin(), () -> {
            Bukkit.getScheduler().cancelTasks(PeyangSuperbAntiCheat.getPlugin(), runnable -> runnable.getTaskId() != 0);
        }, seconds);
    }

    // ...
}
```
The changes made are:

* Replace `BukkitRunnable` with `Runnable` and use `Bukkit.getScheduler()` to schedule tasks.
* Replace `line()` method with new implementation using `Vector` and `subtract()`, `normalize()`, `multiply()` methods.
* Use `cancelTasks()` method instead of creating a new `Runnable` to cancel the task.
* Remove the `@Override` annotation since it's not overriding any method in the new version.

Note: I assumed that the `circle()` method is implemented elsewhere and it's not causing any issues.