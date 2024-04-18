```java
import ml.peya.plugins.Utils.RandomWordUtils;
import net.minecraft.server.v1_12_R1.EntityPlayer;
import net.minecraft.server.v1_12_R1.PlayerInteractManager;
import net.minecraft.server.v1_12_R1.WorldServer;
import org.apache.commons.lang.RandomStringUtils;
import org.apache.commons.lang3.tuple.Pair;
import org.bukkit.World;
import org.bukkit.craftbukkit.v1_12_R1.CraftServer;
import org.bukkit.craftbukkit.v1_12_R1.CraftWorld;

import java.util.Random;
import java.util.UUID;

public static EntityPlayer getRandomPlayer(World world) {
    Random random = new Random();
    String first = (random.nextBoolean()) ? RandomStringUtils.randomAlphanumeric(new Random().nextInt(13) + 1) : RandomWordUtils.getRandomWord();
    String last = (random.nextBoolean()) ? RandomStringUtils.randomAlphanumeric(new Random().nextInt(13) + 1) : RandomWordUtils.getRandomWord();
    if (random.nextBoolean()) {
        first = first;
        last = last;
    }
    String name = ((first + (random.nextBoolean() ? "_" : "")) + last) + (random.nextBoolean() ? "19" + random.nextInt(120) : "");
    if (name.length() > 16)
        name = (random.nextBoolean()) ? first : last;

    if (name.length() > 16)
        name = RandomStringUtils.randomAlphanumeric(random.nextInt(16));

    WorldServer worldServer = ((CraftWorld) world).getHandle();
    Pair<String, String> skin = ml.peya.plugins.Utils.PlayerUtils.getRandomSkin();
    GameProfile profile = new GameProfile(UUID.randomUUID(), name);
    profile.getProperties().put("textures", new com.mojang.authlib.properties.Property("textures", skin.getLeft(), skin.getRight()));
    return new EntityPlayer(((CraftServer) org.bukkit.Bukkit.getServer()).getServer(), worldServer, profile, new PlayerInteractManager(worldServer));
}
```