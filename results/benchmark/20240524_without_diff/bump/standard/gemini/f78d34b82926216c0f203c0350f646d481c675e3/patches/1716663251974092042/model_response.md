```java
public void run() {
    double speed = 0.0;
    if (player.hasMetadata("speed"))
        for (MetadataValue value : player.getMetadata("speed"))
            if (value.getOwningPlugin().getName().equals(PeyangSuperbAntiCheat.getPlugin().getName()))
                speed = value.asDouble() * 2.0;



    for (double i = 0; i < (java.lang.Math.PI * 2); i++) {
        double rangeTmp = radius;
        if (ml.peya.plugins.Variables.config.getBoolean("npc.wave"))
            rangeTmp = ml.peya.plugins.Detect.NPCTeleport.getRangeTmp(rangeTmp, radius);

        final Location center = player.getLocation();
        final Location n = new Location(center.getWorld(), ml.peya.plugins.Detect.NPCTeleport.auraBotXPos(time[0], rangeTmp + speed) + center.getX(), center.getY() + ml.peya.plugins.Detect.NPCTeleport.getWaveY(count[0]), ml.peya.plugins.Detect.NPCTeleport.auraBotZPos(time[0], rangeTmp + speed) + center.getZ(), ((float) (ml.peya.plugins.Detect.NPCTeleport.getYpp(4.5, false))), ((float) (ml.peya.plugins.Detect.NPCTeleport.getYpp(0.01, count[0] < 20))));
        NPC.setLocation(n, target);
        ((CraftPlayer) (player)).getHandle().playerConnection.sendPacket(new PacketPlayOutEntityTeleport(target));
        NPC.setArmor(player, target, arm);
        $missing$ = $missing$.runTask(PeyangSuperbAntiCheat.getPlugin());
        count[0]++;
        CheatDetectNowMeta meta = ml.peya.plugins.Variables.cheatMeta.getMetaByPlayerUUID(player.getUniqueId());
        if (meta == null)
            continue;

        meta.setNpcLocation(n.toVector());
    }
    time[0] += ml.peya.plugins.Variables.config.getDouble("npc.time") + (ml.peya.plugins.Variables.config.getBoolean("npc.speed.wave") ? ml.peya.plugins.Detect.NPCTeleport.getSpeedWave(time[0]) : 0.0);
}
```