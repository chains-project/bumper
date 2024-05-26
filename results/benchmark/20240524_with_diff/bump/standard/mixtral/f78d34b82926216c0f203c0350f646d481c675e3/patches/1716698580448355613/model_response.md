Here've updated the code to use the new library version. I've replaced the old package names with the new ones:

```java
public static net.minecraft.server.v1_12_R1.EntityPlayer getRandomPlayer(org.bukkit.World world) {
    java.util.Random random = new java.util.Random();
    java.lang.String first = (random.nextBoolean()) ? org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(new java.util.Random().nextInt(13) + 
```