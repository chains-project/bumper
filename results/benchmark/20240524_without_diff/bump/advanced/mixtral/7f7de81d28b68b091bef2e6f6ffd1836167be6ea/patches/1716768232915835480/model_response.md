Here's a possible patch for the given code. I've changed the type of the `reg` variable to `Map<MOScope, ManagedObject>` which is the common supertype of `SortedMap<MOScope, ManagedObject>` and `SortedMap<MOScope, ManagedObject<?>>`.

This should fix the incompatible types error you're encountering.
```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        Map<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```
Note: I'm assuming that the `server.getRegistry()` method returns a `SortedMap` with the given types. If this is not the case, you may need to make further adjustments.