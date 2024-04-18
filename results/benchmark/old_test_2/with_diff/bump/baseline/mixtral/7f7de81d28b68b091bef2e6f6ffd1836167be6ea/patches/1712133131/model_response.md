Here's a possible patch that should fix the error:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        Map<MOScope, ManagedObject<?>> unmodifiableReg = Collections.unmodifiableSortedMap(reg);
        registry.set(server, unmodifiableReg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The key change here is to create an unmodifiableSortedMap from the original SortedMap returned by `server.getRegistry()`, and then set that unmodifiable map on the `registry` field. This way, the compiler is happy because it knows that the type of the map being set is compatible with the type of the `registry` field.

Note that this patch assumes that the `server` object has a `getRegistry()` method that returns a `SortedMap` of type `<MOScope, ManagedObject<?>>`. If this is not the case, then the patch may need to be adjusted accordingly.