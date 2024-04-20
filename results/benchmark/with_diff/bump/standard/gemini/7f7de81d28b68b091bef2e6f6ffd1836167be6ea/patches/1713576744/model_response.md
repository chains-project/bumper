```java
private void registerHard(final MOGroup group) {
    try {
        final Field registryField = server.getClass().getDeclaredField("registry");
        registryField.setAccessible(true);
        final SortedMap<MOScope, ManagedObject> registry = (SortedMap<MOScope, ManagedObject>) registryField.get(server);

        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        registry.put(contextScope, group);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
``` 
