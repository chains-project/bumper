Here's the fixed `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        Map<MOScope, ManagedObject<?>> reg = server.getRegistry().values().stream()
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, new TreeMap<>(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The changes are:

1. Replaced `SortedMap` with `Map` when getting the registry value.
2. Converted the registry value to a `Map` and used `Collectors.toMap` to create a new `Map` with the same keys and values.
3. Changed the type of the `reg` variable to `Map<MOScope, ManagedObject<?>>`.
4. Replaced the original `reg` with a new `TreeMap` when setting the registry value.