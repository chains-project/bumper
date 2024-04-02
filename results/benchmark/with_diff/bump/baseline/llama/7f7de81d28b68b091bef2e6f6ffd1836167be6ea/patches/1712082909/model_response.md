Here's a proposed patch to fix the failing client code:
```java
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
The patch removes the unnecessary `SortedMap` type parameter and uses the raw `SortedMap` class instead, which is compatible with the updated library version.

Here's the patch in code format:
```diff
-     final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
+     final SortedMap reg = server.getRegistry();
```