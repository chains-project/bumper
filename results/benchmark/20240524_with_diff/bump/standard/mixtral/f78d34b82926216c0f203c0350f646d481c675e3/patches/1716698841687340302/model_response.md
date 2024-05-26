Here'iv fixed the code by updating the import statements to use the new package name `tokyo.peya.lib`:
```java
import org.apache.commons.lang3.tuple.Pair;
import com.mojang.authlib.GameProfile;
import com.mojang.authlib.properties.Property;
import net.minecraft.server.v1_12_R1.EntityPlayer;
import net.minecraft.server.v1_12_R1.PlayerInteractManager;
import net.minecraft.server.v1_12_R1.WorldServer;
import org.bukkit.Bukkit;
import org.bukkit.craftbukkit.v1_12_R1.CraftServer;
import org.bukkit.craftbukkit.v1_12_tokyo.CraftWorld;import tokyo.peya.lib.LeetConverter;

public static EntityPlayer getRandomPlayer(org.bukkit.World world) {
    java.util.Random random = new java.util.Random();
    java.lang.String first = (random.nextBoolean()) ? org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(new java.util.Random().nextInt(13) + 
```