Here's the fixed version of the `registerHard` method:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final Map<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, new TreeMap<>(reg));
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The changes are:

1. Replace `SortedMap` with `Map` for the type of `reg`.
2. Replace `reg.put(contextScope, group);` with `reg = new TreeMap<>(reg); registry.put(contextScope, group);`.

This solution works because the `SortedMap` interface extends the `Map` interface, so it's safe to use `Map` instead. Also, since the `registry` field in `DefaultMOServer` is a `TreeMap`, we need to convert the `reg` to a `TreeMap` before setting it to the `registry` field.