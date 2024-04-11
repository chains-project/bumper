Here's the fixed `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        Map<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, new TreeMap<>(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The changes are:

1. Replaced `SortedMap` with the raw type `Map` when getting the registry from the server.
2. Created a new `TreeMap` with the same key-value pairs as the registry and set it on the server. This ensures that the registry remains sorted.

This way, you avoid the type mismatch error caused by the change in the library version.