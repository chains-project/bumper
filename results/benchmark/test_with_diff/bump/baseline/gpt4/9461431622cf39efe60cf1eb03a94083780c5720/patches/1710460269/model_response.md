```java
/**
 * Sets the private registry value of {@link DefaultMOServer} via reflection.
 * FIXME
 * If there is any possibility to avoid this, then replace!
 *
 * @param group {@link ManagedObject} to register.
 */
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
In this patch, the only change is in the type of the `reg` SortedMap. It was previously declared as `SortedMap<MOScope, ManagedObject>`, but the error message indicates that it should be `SortedMap<MOScope, ManagedObject<?>>`. This change should resolve the error.