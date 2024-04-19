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
            server.setRegistry(reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```
The `server.getRegistry()` method returns a `SortedMap` of `MOScope` and `ManagedObject`, but the `registry.set()` method expects a `SortedMap` of `MOScope` and `ManagedObject` as its parameter. In order to fix the incompatible types error, we can remove the `registry.set()` method call and instead use the `server.setRegistry()` method to set the `SortedMap` of `MOScope` and `ManagedObject` as the registry of the `server` object.