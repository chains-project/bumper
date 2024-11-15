```java
private void registerHard(final MOGroup group) {
    // Get the server's registry field.
    Field registryField = server.getClass().getDeclaredField("registry");
    registryField.setAccessible(true);

    // Get the server's registry.
    SortedMap<MOScope, ManagedObject> registry = (SortedMap<MOScope, ManagedObject>) registryField.get(server);

    // Create a new context scope for the group.
    DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());

    // Put the group in the registry with the new context scope.
    registry.put(contextScope, group);

    // Set the server's registry back to the field.
    registryField.set(server, registry);
}
```