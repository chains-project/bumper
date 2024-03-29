Here is a possible patch for the given failing code:
```java
import com.mojang.authlib.GameProfile;

// ...

public static GameProfile getGameProfile(String name) {
    return new GameProfile(UUID.nameUUIDFromBytes(name.getBytes()), name);
}
```
Explanation:

* The class `GameProfile` has been moved from `net.minecraft.server.v1_12_R1` to `com.mojang.authlib` package.
* The method `nameUUIDFromBytes(byte[] name)` can be used to generate a UUID from a string name.
* The method `getGameProfile(String name)` has been updated to reflect these changes.