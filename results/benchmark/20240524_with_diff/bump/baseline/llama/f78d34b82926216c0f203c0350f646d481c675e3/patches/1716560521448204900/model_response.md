```java
public static void magic(Player player, int seconds)
{
    final int[] count = {0};
    tokyo.peya.lib.WaveCreator wave = new tokyo.peya.lib.WaveCreator(0.8, 1.8, 0.1);

    BukkitRunnable runnable = new BukkitRunnable()
    {
        @Override
        public void run()
        {
            for (double i = 0; i < Math.PI * 2; i++)
            {
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
            }

            Location center = player.getLocation();

            line(center.clone().add(3, 0.7, 0), center.clone().add(-1.5, 0.7, 2.3));
            line(center.clone().add(-1.5, 0.7, 2.3), center.clone().add(-1.5, 0.7, -2.3));
            line(center.clone().add(3, 0.7, 0), center.clone().add(-1.5, 0.7, -2.3));

            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, -2.3));
            line(center.clone().add(1.5, 0.7, -2.3), center.clone().add(1.5, 0.7, 2.3));
            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, 2.3));
        }
    };

    runnable.runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), 0L, 1L);
    new BukkitRunnable()
    {
        public void run()
        {
            runnable.cancel();
        }
    }.runTaskLater(PeyangSuperbAntiCheat.getPlugin(), seconds);
}
```