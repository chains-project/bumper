```java
public static EntityPlayer getRandomPlayer(World world)
{
    Random random = new Random();
    String first = random.nextBoolean()
        ? RandomStringUtils.randomAlphanumeric(new Random().nextInt(13) + 1)
        : RandomWordUtils.getRandomWord();
    String last = random.nextBoolean()
        ? RandomStringUtils.randomAlphanumeric(new Random().nextInt(13) + 1)
        : RandomWordUtils.getRandomWord();

    if (random.nextBoolean())
    {
        first = first.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5").replace("t", "7");
        last = last.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5").replace("t", "7");
    }

    String name = first + (random.nextBoolean() ? "_": "") + last + (random.nextBoolean() ? "19" + random.nextInt(120): "");
    if (name.length() > 16)
        name = random.nextBoolean() ? first: last;

    if (name.length() > 16)
        name = RandomStringUtils.randomAlphanumeric(random.nextInt(16));

    WorldServer worldServer = ((CraftWorld) world).getHandle();

    Pair<String, String> skin = getRandomSkin();

    GameProfile profile = new GameProfile(UUID.randomUUID(), name);

    profile.getProperties().put("textures", new Property("textures", skin.getLeft(), skin.getRight()));

    return new EntityPlayer(
        ((CraftServer) Bukkit.getServer()).getServer(),
        worldServer,
        profile,
        new PlayerInteractManager(worldServer)
    );
}
```