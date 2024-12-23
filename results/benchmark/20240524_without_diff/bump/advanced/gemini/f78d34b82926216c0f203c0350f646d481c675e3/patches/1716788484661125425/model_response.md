```java
import com.google.common.collect.ImmutableList;
import develop.p2p.lib.WaveCreator;
import java.util.List;
import net.minecraft.server.v1_8_R3.PacketPlayOutWorldParticles;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Particle;
import org.bukkit.craftbukkit.v1_8_R3.entity.CraftPlayer;
import org.bukkit.entity.Player;

public class Decorations {
    private static final List<Particle> PARTICLE_LIST = ImmutableList.of(Particle.FLAME, Particle.REDSTONE, Particle.SMOKE_NORMAL, Particle.SMOKE_LARGE, Particle.EXPLOSION_NORMAL, Particle.EXPLOSION_HUGE, Particle.FIREWORKS_SPARK, Particle.CRIT, Particle.CRIT_MAGIC, Particle.SPELL, Particle.SPELL_INSTANT, Particle.SPELL_MOB, Particle.SPELL_MOB_AMBIENT, Particle.SPELL_WITCH, Particle.DRAGON_BREATH, Particle.END_ROD, Particle.ENCHANTMENT_TABLE, Particle.SNOWBALL, Particle.SNOW_SHOVEL, Particle.SLIME, Particle.HEART, Particle.ANGRY_VILLAGER, Particle.HAPPY_VILLAGER);

    public static void playParticle(final Player player, final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ, final float speed, final int amount) {
        WaveCreator.sendWave(player, new WaveCreator.Wave() {
            @Override
            public void sendPacket(final Player player) {
                final PacketPlayOutWorldParticles packet = new PacketPlayOutWorldParticles(particle, true, (float)location.getX() + offsetX, (float)location.getY() + offsetY, (float)location.getZ() + offsetZ, speed, amount, 0.0f, 0.0f, 0.0f, 0.0f, 1);
                ((CraftPlayer)player).getHandle().playerConnection.sendPacket(packet);
            }
        });
    }

    public static void playParticleAll(final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ, final float speed, final int amount) {
        WaveCreator.sendWaveAll(new WaveCreator.Wave() {
            @Override
            public void sendPacket(final Player player) {
                final PacketPlayOutWorldParticles packet = new PacketPlayOutWorldParticles(particle, true, (float)location.getX() + offsetX, (float)location.getY() + offsetY, (float)location.getZ() + offsetZ, speed, amount, 0.0f, 0.0f, 0.0f, 0.0f, 1);
                ((CraftPlayer)player).getHandle().playerConnection.sendPacket(packet);
            }
        });
    }

    public static void playParticle(final Player player, final Particle particle, final Location location) {
        playParticle(player, particle, location, 0.0f, 0.0f, 0.0f, 0.0f, 1);
    }

    public static void playParticleAll(final Particle particle, final Location location) {
        playParticleAll(particle, location, 0.0f, 0.0f, 0.0f, 0.0f, 1);
    }

    public static void playRandomParticle(final Player player, final Location location) {
        playParticle(player, PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location);
    }

    public static void playRandomParticleAll(final Location location) {
        playParticleAll(PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location);
    }

    public static void playParticle(final Player player, final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ) {
        playParticle(player, particle, location, offsetX, offsetY, offsetZ, 0.0f, 1);
    }

    public static void playParticleAll(final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ) {
        playParticleAll(particle, location, offsetX, offsetY, offsetZ, 0.0f, 1);
    }

    public static void playRandomParticle(final Player player, final Location location, final float offsetX, final float offsetY, final float offsetZ) {
        playParticle(player, PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location, offsetX, offsetY, offsetZ);
    }

    public static void playRandomParticleAll(final Location location, final float offsetX, final float offsetY, final float offsetZ) {
        playParticleAll(PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location, offsetX, offsetY, offsetZ);
    }

    public static void playParticle(final Player player, final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ, final int amount) {
        playParticle(player, particle, location, offsetX, offsetY, offsetZ, 0.0f, amount);
    }

    public static void playParticleAll(final Particle particle, final Location location, final float offsetX, final float offsetY, final float offsetZ, final int amount) {
        playParticleAll(particle, location, offsetX, offsetY, offsetZ, 0.0f, amount);
    }

    public static void playRandomParticle(final Player player, final Location location, final float offsetX, final float offsetY, final float offsetZ, final int amount) {
        playParticle(player, PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location, offsetX, offsetY, offsetZ, amount);
    }

    public static void playRandomParticleAll(final Location location, final float offsetX, final float offsetY, final float offsetZ, final int amount) {
        playParticleAll(PARTICLE_LIST.get((int)(Math.random() * (double)PARTICLE_LIST.size())), location, offsetX, offsetY, offsetZ, amount);
    }
}
```