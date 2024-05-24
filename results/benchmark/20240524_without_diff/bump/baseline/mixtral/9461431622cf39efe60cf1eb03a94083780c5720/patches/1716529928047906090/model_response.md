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

The change is in the `SortedMap` declaration, where we now use `SortedMap<MOScope, ManagedObject<?>>` instead of `SortedMap<MOScope, ManagedObject>`. This change is necessary because the new library version uses generics for the `ManagedObject` type.