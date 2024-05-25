Here's a proposed patch for the failing client code:

```java
public static void magic(Player player, int seconds)
{
    final int[] count = {0};
    WaveCreator wave = new WaveCreator(0.8, 1.8, 0.1);

    Runnable runnable = new Runnable()
    {
        @Override
        public void run()
        {
            for (double i = 0; i < Math.PI * 2; i++)
            {
                Location center = player.getLocation();

                circle(center.clone().add(0, 0.9, 0), count[0], 3, "CRIT");

                circle(center.add(0, 0.7, 0), count[0], 2.7, "ENCHANTMENT_TABLE");

                circle(center.clone().add(0, wave.get(0.01, false), 0), count[0], wave.getStatic());

                circle(center.clone().add(3.2, 0.7, 3.2), count[0], 1.5);
                circle(center.clone().add(-3.2, 0.7, -3.2), count[0], 1.5);
                circle(center.clone().add(-3.2, 0.7, 3.2), count[0], 1.5);
                circle(center.clone().add(3.2, 0.7, -3.2), count[0], 1.5);

                circle(center.clone().add(0, 1.5, 0), count[0], 5, "SPELL_WITCH");

                count[0]++;
            }

            Location center = player.getLocation();

            line(center.clone().add(3, 0.7, 0), center.clone().add(-1.5, 0.7, 2.3));
            line(center.clone().add(-1.5, 0.7, 2.3), center.clone().add(-1.5, 0.7, -2.3)); //三角
            line(center.clone().add(3, 0.7, 0), center.clone().add(-1.5, 0.7, -2.3));

            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, -2.3));
            line(center.clone().add(1.5, 0.7, -2.3), center.clone().add(1.5, 0.7, 2.3)); //三角(反転)
            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, 2.3));
        }
    };

    new BukkitRunnable()
    {
        @Override
        public void run()
        {
            runnable.run();
        }
    }.runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), 0L, 1L);

    new BukkitRunnable()
    {
        @Override
        public void run()
        {
            runnable.run();
        }
    }.runTaskLater(PeyangSuperbAntiCheat.getPlugin(), seconds * 20L);

}
```

The main changes are:

* Replace the `BukkitRunnable` class with the standard `Runnable` interface.
* Replace the `Particle` enum with a string representation of the particle type.
* Change the delay time for the second `BukkitRunnable` from `seconds` to `seconds * 20L` to convert from seconds to ticks.