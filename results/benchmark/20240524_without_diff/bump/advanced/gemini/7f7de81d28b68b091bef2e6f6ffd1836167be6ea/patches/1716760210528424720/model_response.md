```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
        final MOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        final ManagedObject mo = reg.put(contextScope, group);
        if (mo != null) {
            reg.put(contextScope, mo);
        }
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```