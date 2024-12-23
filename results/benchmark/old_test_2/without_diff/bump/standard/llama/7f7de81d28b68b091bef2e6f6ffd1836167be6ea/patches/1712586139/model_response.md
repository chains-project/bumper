Here's a proposed patch to fix the error:
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
            reg.put(contextScope, group);
            // Fix: Use method reference to avoid incompatible types
            registry.set(server, reg, SortedMap::new);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```
The change is in the last line, where we use the `SortedMap::new` method reference to create a new `SortedMap` instance, instead of directly calling the constructor. This avoids the incompatible types issue.