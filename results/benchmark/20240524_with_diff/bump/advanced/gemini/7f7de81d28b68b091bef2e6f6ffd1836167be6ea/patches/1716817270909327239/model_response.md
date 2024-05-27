```java
private void registerHard(final MOGroup group) {
    try {
        // Get the private registry field of DefaultMOServer using reflection
        final Field registryField = server.getClass().getDeclaredField("registry");
        registryField.setAccessible(true);

        // Get the current registry value
        final SortedMap<MOScope, ManagedObject> currentRegistry = (SortedMap<MOScope, ManagedObject>) registryField.get(server);

        // Create a new context scope with the group's scope
        final MOScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());

        // Put the group into the new registry with the context scope as the key
        final SortedMap<MOScope, ManagedObject> newRegistry = new TreeMap<>(currentRegistry);
        newRegistry.put(contextScope, group);

        // Set the new registry value back to the DefaultMOServer instance
        registryField.set(server, newRegistry);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```