Here's a possible patch for the `registerHard` method. The issue is caused by a type mismatch between the declared type of the `reg` variable and the returned type of the `server.getRegistry()` method. The solution is to change the type of the `reg` variable to the raw type `SortedMap`, which is the nearest common ancestor of `SortedMap<MOScope, ManagedObject<T>>` and `SortedMap<MOScope, ManagedObject>`.

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```