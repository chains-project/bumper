Here'd a patch that replaces the dependency on `develop.p2p.lib.LeetConverter` with the new library' `tokyo.peya.lib.LeetConverter`:
```java
public static net.minecraft.server.v1_12_R1.EntityPlayer getRandomPlayer(org.bukkit.World world) {
    java.util.Random random = new java.util.Random();
    java.lang.String first = (random.nextBoolean()) ? org.apache.commons.lang.RandomStringUtils.randomAlphanumeric(new java.util.Random().nextInt(13) + 
```