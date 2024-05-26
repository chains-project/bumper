Here'F the updated `registerHard` method that should fix the type compatibility issue:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        SortedMap<MOScope, ManagedObject> oldReg = server.getRegistry();
        @SuppressWarnings("unchecked")
        SortedMap<MOScope, ManagedObject<?>> newReg = (SortedMap<MOScope, MangedObject<?>>) oldReg;
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        newReg.put(contextScope, group);
        registry.set(server, newReg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
 }
}
```

The changes include:

1. Adding a new variable `oldReg` to store the original `SortedMap<MOScope, ManagedObject>` from `server.getRegistry()`.
2. Casting `oldReg` to `SortedMap<MOScope, ManagedObject<?>>` and storing it in `newReg`.
3. Replacing the usage of `reg` with `newReg` for adding the new `MOGroup` to the registry.

These changes should resolve the type compatibility issue.