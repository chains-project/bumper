Here's a fixed version of the `registerHard` method. I changed the type of the `reg` variable to `Map<MOScope, ManagedObject>` to match the expected type in the error message:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final Map<MOScope, ManagedObject> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

This should resolve the type mismatch error. However, note that this change might cause issues elsewhere in the code if the registry's type is expected to be `SortedMap`. In that case, you may need to reconsider the design of the code and avoid using reflection to set the registry value.