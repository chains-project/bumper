```java
  /**
     * AuraBotのテレポート。
     *
     * @param player    プレイヤー。
     * @param target    ターゲット。
     * @param arm       装備。
     * @param reachMode リーチモードかどうか。
     */
    private static void auraBotTeleport(Player player, EntityPlayer target, ItemStack[] arm, boolean reachMode)
    {
        final double[] time = {0.0};
        final double radius = reachMode ? config.getDouble("npc.reachRange"): config.getDoubleList("npc.range")
            .get(new Random().nextInt(config.getDoubleList("npc.range").size()));

        WaveCreator ypp = new WaveCreator(10.0, 100.0, 10.0);

        final int[] count = {0};
        BukkitRunnable r = new BukkitRunnable()
        {
            public void run()
            {
                double speed = 0.0;

                if (player.hasMetadata("speed"))
                    for (MetadataValue value : player.getMetadata("speed"))
                        if (value.getOwningPlugin().getName().equals(PeyangSuperbAntiCheat.getPlugin().getName()))
                            speed = value.asDouble() * 2.0;
                for (double i = 0; i < Math.PI * 2; i++)
                {
                    double rangeTmp = radius;

                    if (config.getBoolean("npc.wave"))
                        rangeTmp = new WaveCreator(radius - 0.1, radius, config.getDouble("npc.waveMin"))
                            .get(0.01, true);

                    final Location center = player.getLocation();
                    final Location n = new Location(
                        center.getWorld(),
                        auraBotXPos(time[0], rangeTmp + speed) + center.getX(),
                        center.getY() + new WaveCreator(1.0, 2.0, 0.0).get(0.01, count[0] < 20),
                        auraBotZPos(time[0], rangeTmp + speed) + center.getZ(),
                        (float) ypp.getStatic(),
                        (float) ypp.get(4.5, false)
                    );

                    NPC.setLocation(n, target);
                    // ((CraftPlayer) player).getHandle().playerConnection
                    //     .sendPacket(new PacketPlayOutEntityTeleport(target));

                    NPC.setArmor(player, target, arm);
                    new BukkitRunnable()
                    {
                        @Override
                        public void run()
                        {
                            Bukkit.getOnlinePlayers()
                                .parallelStream()
                                .filter(p -> p.hasPermission("psac.viewnpc"))
                                .forEachOrdered(p ->
                                {
                                    // ((CraftPlayer) p).getHandle().playerConnection
                                    //     .sendPacket(new PacketPlayOutEntityTeleport(target));
                                    NPC.setArmor(p, target, arm);
                                });
                            this.cancel();
                        }
                    }.runTask(PeyangSuperbAntiCheat.getPlugin());
                    count[0]++;
                    CheatDetectNowMeta meta = cheatMeta.getMetaByPlayerUUID(player.getUniqueId());
                    if (meta == null) continue;
                    meta.setNpcLocation(n.toVector());
                }
                time[0] += config.getDouble("npc.time") + (config.getBoolean("npc.speed.wave")
                    ? new WaveCreator(0.0, config.getDouble("npc.speed.waveRange"), 0 - config.getDouble("npc.speed.waveRange")).get(0.001, true)
                    : 0.0);
            }
        };
        r.runTaskTimer(PeyangSuperbAntiCheat.getPlugin(), 0, 1);

        new BukkitRunnable()
        {
            @Override
            public void run()
            {
                r.cancel();
                this.cancel();
            }
        }.runTaskLater(PeyangSuperbAntiCheat.getPlugin(), 20 * (config.getLong("npc.seconds")));

    }
```