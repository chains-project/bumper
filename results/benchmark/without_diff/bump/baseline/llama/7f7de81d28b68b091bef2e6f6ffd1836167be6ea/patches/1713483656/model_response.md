```
    private void registerHard(final MOGroup group) {
        try {
            final Field registry = server.getClass().getDeclaredField("registry");
            registry.setAccessible(true);
            final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            reg.put(contextScope, group);
            registry.set(server, reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```

Replace with:
```
    private void registerHard(final MOGroup group) {
        try {
            final Field registry = server.getClass().getDeclaredField("registry");
            registry.setAccessible(true);
            final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            reg.put(contextScope, group);
            // registry.set(server, reg);
            Field modifiableRegistryField = server.getClass().getSuperclass().getDeclaredField("modifiableRegistry");
            modifiableRegistryField.setAccessible(true);
            modifiableRegistryField.set(server, reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```

The `registry` field is not accessible in the current class, so we need to find another way to set its value. We can do this by accessing the `modifiableRegistry` field, which is accessible and can be set to the desired value.


Note that we're using the `getSuperclass()` method to access the `modifiableRegistry` field, since it's not available in the current class.