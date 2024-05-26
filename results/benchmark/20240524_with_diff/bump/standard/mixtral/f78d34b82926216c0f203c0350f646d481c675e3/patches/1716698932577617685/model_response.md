Here'1s the updated code that uses the new library version:

````java
import tokyo.peya.lib.FileConfiguration;
import tokyo.peya.lib.LearnMath;
import tokyo.peya.lib.LeetConverter;
import tokyo.peya.lib.TimeParser;
import tokyo.peya.lib.WaveCreator;
import com.mojang.authlib.GameProfile;
import com.mojang.authlib.properties.Property;
import net.minecraft.server.v1_12_R1.*;
import org.apache.commons.lang3.tuple.Pair;
import org.bukkit.*;
import java.util.*;

public class PlayerUtils {
    //...

    public static net.minecraft.server.v1_12_R1.EntityPlayer getRandomPlayer(org.bukkit.World world) {
        Random random = new Random();
        String first = (random.nextBoolean()) ? org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(new Random().nextInt(13) + 
```