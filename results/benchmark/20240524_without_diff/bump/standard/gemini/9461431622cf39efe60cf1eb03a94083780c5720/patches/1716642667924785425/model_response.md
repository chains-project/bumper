```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
        final MOScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        final ManagedObject managedObject = reg.get(contextScope);
        if (managedObject != null) {
            reg.remove(contextScope);
        }
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```