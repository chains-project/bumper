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
            final SortedMap<MOScope, ManagedObject<?>> reg = (SortedMap<MOScope, ManagedObject<?>>) server.getRegistry();
            DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
            reg.put(contextScope, group);
            registry.set(server, reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```
In the original code, the type of the SortedMap `reg` was declared without the wildcard `<?>`. This caused a type mismatch error because the `server.getRegistry()` method returns a SortedMap with a wildcard in its value type. The solution is to add the wildcard `<?>` to the declaration of `reg`.