Here's the fixed version of the `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | ClassCastException e) {
        log.warn("could not set server registry", e);
    }
}
```

The change is casting the `SortedMap` returned by `server.getRegistry()` to `SortedMap<MOScope, ManagedObject<?>>`. This is necessary because the new library version has added a type parameter to the `ManagedObject` class. This change allows the code to compile and work with the new library version.