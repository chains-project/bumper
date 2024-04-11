Here's a fixed version of the `registerHard` method that should resolve the type mismatch error caused by the updated library version:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final Map<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, new TreeMap<>(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The changes include:

1. Changed the type of the `reg` variable from `SortedMap` to the raw `Map` type, since the raw type is a common supertype of both `SortedMap` and the updated library's `SortedRegistry`.
2. Wrapped the `reg` variable with a `TreeMap` when setting it back to the `registry` field, to ensure that the registry maintains a sorted order based on the natural ordering of `MOScope`.

These changes ensure that the code remains compatible with both the old and new versions of the library.