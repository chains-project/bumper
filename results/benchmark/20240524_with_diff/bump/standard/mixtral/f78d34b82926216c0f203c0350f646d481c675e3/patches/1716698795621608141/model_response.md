Here'd a patch for the code that replaces the old library with the new one:

```java
import tokyo.peya.lib.LeetConverter;
import tokyo.peya.lib.bukkit.exception.SelectorInvalidException;
import tokyo.peya.lib.FileConfiguration;
import tokyo.peya.lib.LearnMath;
import tokyo.peya.lib.TimeParser;
import tokyo.peya.lib.WaveCreator;

public static net.minecraft.server.v1_12_R1.EntityPlayer getRandomPlayer(org.bukkit.World world) {
    java.util.Random random = new java.util.Random();
    java.lang.String first = (random.nextBoolean()) ? org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(new java.util.Random().nextInt(13) + 
```