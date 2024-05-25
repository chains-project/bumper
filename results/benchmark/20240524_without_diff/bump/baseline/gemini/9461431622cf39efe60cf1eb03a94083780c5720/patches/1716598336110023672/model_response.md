```java
  /**
     * Sets the private registry value of {@link DefaultMOServer} via reflection.
     * FIXME
     * If there is any possibility to avoid this, then replace!
     *
     * @param group {@link ManagedObject} to register.
     */
    private void registerHard(final MOGroup group) {
        try {
            final Field registry = server.getClass().getDeclaredField("registry");
            registry.setAccessible(true);
            final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            // Cast the registry to the correct type
            SortedMap<MOScope, ManagedObject<?>> typedRegistry = (SortedMap<MOScope, ManagedObject<?>>) reg;
            typedRegistry.put(contextScope, group);
            registry.set(server, typedRegistry);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```