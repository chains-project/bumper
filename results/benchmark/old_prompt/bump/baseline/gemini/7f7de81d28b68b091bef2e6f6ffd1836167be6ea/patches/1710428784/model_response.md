```java
private void registerHard(final MOGroup group) {
        try {
            final Field registry = server.getClass().getDeclaredField("registry");
            registry.setAccessible(true);
            // Get the existing registry
            final SortedMap<MOScope, ManagedObject<?>> reg = (SortedMap<MOScope, ManagedObject<?>>) registry.get(server);
            // Create a new context scope
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            // Put the new group into the registry
            reg.put(contextScope, group);
            // Set the registry back into the server
            registry.set(server, reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```