Here'v a suggested patch for the `registerHard` method. It seems that the issue is caused by incompatible types in the `SortedMap` used for the registry. To fix this, you can use the diamond operator (<>) to let the compiler infer the correct type.

Note that I'd recommend a more robust solution if possible, such as using the library's provided API for registering the `MOGroup` instead of accessing and modifying the registry directly.

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject<?>> registryValue = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        registryValue.put(contextScope, group);
        registry.set(server, registryValue);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("Could not set server registry", e);
    }
}
``
```