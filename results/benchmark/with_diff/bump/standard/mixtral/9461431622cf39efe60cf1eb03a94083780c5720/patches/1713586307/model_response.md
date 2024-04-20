Here's a fixed version of the `registerHard` method that should resolve the type mismatch error:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The change I made is to specify the wildcard `?` in the type parameter of `SortedMap<MOScope, ManagedObject<?>>` when getting the registry from the server. This allows the registry to be assigned to a variable of type `SortedMap<MOScope, ManagedObject<?>>`, which is compatible with the type of the `reg` variable.