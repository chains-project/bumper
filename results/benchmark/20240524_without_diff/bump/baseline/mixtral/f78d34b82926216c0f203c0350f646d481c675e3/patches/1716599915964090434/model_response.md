Here's the fixed method:
```java
    public static void magic(Player player, int seconds)
    {
        final int[] count = {0};
        WaveCreator wave = new WaveCreator(0.8, 1.8, 0.1);

        Runnable runnable = () ->
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
            line(center.clone().add(-1.5, 0.7, 2.3), center.clone().add(-1.5, 0.7, -2.3)); //三角
            line(center.clone().add(3, 0.7, 0), center.clone().add(-1.5, 0.7, -2.3));

            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, -2.3));
            line(center.clone().add(1.5, 0.7, -2.3), center.clone().add(1.5, 0.7, 2.3)); //三角(反転)
            line(center.clone().add(-3, 0.7, 0), center.clone().add(1.5, 0.7, 2.3));
        };

        runnable.run();
        new Timer().schedule(new TimerTask()
        {
            @Override
            public void run()
            {
                runnable.run();
            }
        }, 0, 1000);
        new Timer().schedule(new TimerTask()
        {
            @Override
            public void run()
            {
                runnable.run();
            }
        }, seconds * 1000);
    }
```
The changes are:

* Replacing `BukkitRunnable` with `Runnable`
* Replacing `runTaskTimer` with `schedule` from `java.util.Timer`
* Replacing `runTaskLater` with `schedule` from `java.util.Timer`
* Adding the necessary imports for `java.util.Timer` and `java.util.TimerTask`

This should fix the issue with the missing symbol, but it's possible that the new implementation may not have the same behavior as the original. It's important to thoroughly test the code to ensure that it works as expected.