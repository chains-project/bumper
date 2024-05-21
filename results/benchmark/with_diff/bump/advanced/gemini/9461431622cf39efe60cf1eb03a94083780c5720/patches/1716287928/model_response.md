```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
        final DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        final ManagedObject<?> managedObject = group;
        reg.put(contextScope, managedObject);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```