Here's a patch to fix the error:

```java
private static void auraBotTeleport(Player player, EntityPlayer target, ItemStack[] arm, boolean reachMode) {
    final double[] time = {0.0};
    final double radius = reachMode ? config.getDouble("npc.reachRange"): config.getDoubleList("npc.range")
        .get(new Random().nextInt(config.getDoubleList("npc.range").size()));

    WaveCreator ypp = new WaveCreator(10.0, 10.0, 10.0);

    final int[] count = {0};
    BukkitRunnable r = new BukkitRunnable() {
        double speed = 0.0;

        @Override
        public void run() {
            if (player.hasMetadata("speed"))
                for (MetadataValue value : player.getMetadata("speed"))
                    if (value.getOwningPlugin().getName().equals(PeyangSuperbAntiCheat.getPlugin().getName()))
                        speed = value.asDouble() * 2.0;
            // ... rest of the code ...
        }
    };
    r.runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), 0, 1);

    new BukkitRunnable() {
        @Override
        public void run() {
            r.cancel();
            this.cancel();
        }
    }.runTaskLater(PeyangSuperbAntiCheat.getPlugin(), 20 * (config.getLong("npc.seconds")));

}
```

The change is moving the `speed` variable inside the `BukkitRunnable` anonymous class, so it can be accessed within the `run()` method.