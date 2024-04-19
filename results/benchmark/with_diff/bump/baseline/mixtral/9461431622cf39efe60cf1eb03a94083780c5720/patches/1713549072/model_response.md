Here's the fixed version of the `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        Map<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, new TreeMap<>(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

Changes made:

1. Changed the type of `reg` from `SortedMap` to `Map` to make it compatible with the new library version.
2. Wrapped the `reg` with a `TreeMap` when setting it back to the `registry` field, as the new version of the library expects a `SortedMap`. This ensures backward compatibility with the old code.

This should resolve the compilation error.