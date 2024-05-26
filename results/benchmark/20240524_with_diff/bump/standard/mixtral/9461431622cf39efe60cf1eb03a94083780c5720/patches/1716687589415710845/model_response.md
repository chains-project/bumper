Here's the fixed `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        @SuppressWarnings("unchecked")
        final SortedMap<MOScope, ManagedObject<MOScope>> reg = (SortedMap<MOScope, ManagedObject<MOScope>>) server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | ClassCastException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The change is to suppress the unchecked cast warning when downcasting the `SortedMap` returned by `server.getRegistry()`. The error occurs because the new library version has added a type parameter to the `ManagedObject` interface.