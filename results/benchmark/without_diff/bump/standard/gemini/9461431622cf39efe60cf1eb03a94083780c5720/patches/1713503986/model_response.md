```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
        // ++ Added method to cast the map to the desired type
        final SortedMap<MOScope, ManagedObject<?>> castedReg = (SortedMap<MOScope, ManagedObject<?>>) reg;
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        castedReg.put(contextScope, group);
        registry.set(server, castedReg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```