Here's a fixed version of the `registerHard` method that should resolve the type mismatch error caused by the library update:

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

The changes made include:

1. Replacing the `SortedMap` type with the raw `Map` type for the `reg` variable. This is safe because the `put` method of the `Map` interface guarantees that the iteration order will be the same as the order of insertion.
2. Creating a new `TreeMap` with the same key-value mappings as `reg` before setting it to the `registry` field. This ensures that the registry remains sorted as required by the library.

These changes ensure that the code is compatible with both the old and new versions of the library.