Here'`Enter` a possible patch for the failing method. The issue is caused by the incompatible types of the SortedMap. The new version of the library removed the generic type from the ManagedObject, so we need to change the type of the SortedMap accordingly.

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ? extends ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```
I changed the type of the `reg` variable to `SortedMap<MOScope, ? extends ManagedObject>`. This way, we can still put the `group` object into the registry, but we don'

```