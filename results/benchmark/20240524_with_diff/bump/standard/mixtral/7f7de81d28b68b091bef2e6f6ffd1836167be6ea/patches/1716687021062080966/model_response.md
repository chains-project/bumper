Here'`enter code here`s the updated `registerHard` method that should fix the type compatibility issue:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ? extends ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctedString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The change is in the type of the `reg` variable. I replaced `SortedMap<MOScope, ManagedObject>` with `SortedMap<MOScope, ? extends ManagedObject>` to allow the use of a wildcard. This way, the compiler won's throw an error related to incompatible types.