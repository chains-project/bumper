Here's a fixed version of the `registerHard` method. I've added a type parameter to the `SortedMap` to ensure type compatibility:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The change is on line 5, where I added the `<? extends ManagedObject>` type parameter to the `SortedMap`. This ensures that the `SortedMap` uses the correct type of `ManagedObject` and prevents the type incompatibility error.