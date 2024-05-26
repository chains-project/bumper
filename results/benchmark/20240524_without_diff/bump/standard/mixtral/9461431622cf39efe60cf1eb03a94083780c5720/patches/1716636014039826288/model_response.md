Here'v a suggested patch for the `registerHard` method. The issue is caused by incompatible types in the `SortedMap` used as the value for the `reg` variable.

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject<?>> reg = new TreeMap<>();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        Field field = server.getClass().getDeclaredField("registry");
        field.setAccessible(true);
        field.set(server, Collections.unmodifiableSortedMap(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
 }
}
``0   
```

The main changes are:

1. Replacing the `SortedMap` instantiation with a `TreeMap` that uses the raw types.
2. Creating a new `SortedMap` instance for `reg` and using `put` to add the `contextScope` and `group`.
3. Replacing the `server.getRegistry()` with a new `SortedMap` instance (`reg`).
4. Using `Collections.unmodifiableSortedMap` to wrap the `reg` before setting it to the `server` instance.

These changes should resolve the incompatible types issue and make the code work with the updated library.

Keep in mind that using raw types can lead to other issues and should be avoided if possible. However, in this case, it is necessary to maintain compatibility with the library.