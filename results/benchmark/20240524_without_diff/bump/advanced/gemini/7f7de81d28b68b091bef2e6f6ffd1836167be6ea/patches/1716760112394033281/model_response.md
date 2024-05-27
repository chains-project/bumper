```java
private void registerHard(final MOGroup group) {
    try {
        final Field registryField = server.getClass().getDeclaredField("registry");
        registryField.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registryField.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```