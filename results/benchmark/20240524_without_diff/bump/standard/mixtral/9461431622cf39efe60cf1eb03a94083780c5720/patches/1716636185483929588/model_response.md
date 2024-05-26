Here'v a suggested patch for the `registerHard` method. The issue seems to be caused by a change in the generic type of the `SortedMap` in the new version of the dependency. We can resolve this by using a `TreeMap` instead of the raw type `SortedMap`.

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject<?>> reg = new TreeMap<>(server.getRegistry());
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
   11 } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

In this updated code, I've created a new `TreeMap` instance with the same key-value pairs as the original `SortedMap`. This ensures that the generic type information is preserved.

Note that the `?` wildcard is used in the value type of the `SortedMap` to denote that the specific type is not known. This should not cause any issues as long as the value is used as a `ManagedObject`.