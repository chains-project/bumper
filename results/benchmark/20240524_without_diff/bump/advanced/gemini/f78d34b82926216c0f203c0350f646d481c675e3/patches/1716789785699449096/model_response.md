```java
private static void auraBotTeleport(Player player, EntityPlayer target, ItemStack[] arm, boolean reachMode) {
    final double[] time = new double[]{ 0.0 };
    final double radius = (reachMode) ? ml.peya.plugins.Variables.config.getDouble("npc.reachRange") : ml.peya.plugins.Variables.config.getDoubleList("npc.range").get(new java.util.Random().nextInt(ml.peya.plugins.Variables.config.getDoubleList("npc.range").size()));
    final int[] count = new int[]{ 0 };
    BukkitRunnable r = new BukkitRunnable() {
        public void run() {
            double speed = 0.0;
            if (player.hasMetadata("speed"))
                for (MetadataValue value : player.getMetadata("speed"))
                    if (value.getOwningPlugin().getName().equals(PeyangSuperbAntiCheat.getPlugin().getName()))
                        speed = value.asDouble() * 2.0;



            for (double i = 0; i < (java.lang.Math.PI * 2); i++) {
                double rangeTmp = radius;
                if (ml.peya.plugins.Variables.config.getBoolean("npc.wave"))
                    rangeTmp = ml.peya.plugins.Detect.NPCTeleport.wave(radius - 0.1, radius, ml.peya.plugins.Variables.config.getDouble("npc.waveMin"), 0.01, true);

                final Location center = player.getLocation();
                final Location n = new Location(center.getWorld(), ml.peya.plugins.Detect.NPCTeleport.auraBotXPos(time[0], rangeTmp + speed) + center.getX(), center.getY() + ml.peya.plugins.Detect.NPCTeleport.wave(1.0, 2.0, 0.0, 0.01, count[0] < 20), ml.peya.plugins.Detect.NPCTeleport.auraBotZPos(time[0], rangeTmp + speed) + center.getZ(), ((float) (0.0)), ((float) (0.0)));
                NPC.setLocation(n, target);
                ((CraftPlayer) (player)).getHandle().playerConnection.sendPacket(new PacketPlayOutEntityTeleport(target));
                NPC.setArmor(player, target, arm);
                new BukkitRunnable() {
                    @java.lang.Override
                    public void run() {
                        Bukkit.getOnlinePlayers().parallelStream().filter(( p) -> p.hasPermission("psac.viewnpc")).forEachOrdered(( p) -> {
                            ((CraftPlayer) (p)).getHandle().playerConnection.sendPacket(new PacketPlayOutEntityTeleport(target));
                            NPC.setArmor(p, target, arm);
                        });
                        this.cancel();
                    }
                }.runTask(PeyangSuperbAntiCheat.getPlugin());
                count[0]++;
                CheatDetectNowMeta meta = ml.peya.plugins.Variables.cheatMeta.getMetaByPlayerUUID(player.getUniqueId());
                if (meta == null)
                    continue;

                meta.setNpcLocation(n.toVector());
            }
            time[0] += ml.peya.plugins.Variables.config.getDouble("npc.time") + (ml.peya.plugins.Variables.config.getBoolean("npc.speed.wave") ? ml.peya.plugins.Detect.NPCTeleport.wave(0.0, ml.peya.plugins.Variables.config.getDouble("npc.speed.waveRange"), 0 - ml.peya.plugins.Variables.config.getDouble("npc.speed.waveRange"), 0.001, true) : 0.0);
        }
    };
    r.runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), 0, 1);
    new BukkitRunnable() {
        @java.lang.Override
        public void run() {
            r.cancel();
            this.cancel();
        }
    }.runTaskLater(PeyangSuperbAntiCheat.getPlugin(), 20 * ml.peya.plugins.Variables.config.getLong("npc.seconds"));
}
```