Here is a possible patch for the code:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        TypeToken<SortedMap<MOScope, ManagedObject<?>>> typeToken = new TypeToken<SortedMap<MOScope, ManagedObject<?>>>(){};
        Map<MOScope, ManagedObject<?>> uncheckedReg = (Map<MOScope, ManagedObject<?>>) reg; // unchecked cast
        SortedMap<MOScope, ManagedObject<?>> unmodifiableReg = Collections.unmodifiableSortedMap(uncheckedReg);
        registry.set(server, unmodifiableReg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The patch uses a type token and an unchecked cast to convert the `SortedMap` returned by `server.getRegistry()` to a `SortedMap<MOScope, ManagedObject<?>>`. It then creates an unmodifiable view of the map and sets it as the new registry value.

Note that this patch uses an unchecked cast and a raw type, which may not be ideal. It is recommended to use a more type-safe solution if possible.