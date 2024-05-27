Here's a patch that should fix the error by using a generic type for the SortedMap:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        @SuppressWarnings("unchecked")
        final SortedMap<MOScope, ManagedObject<ManagedObject>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```
The change is to add a generic type parameter to the `SortedMap` declaration, which should make the cast in the original code unnecessary.

Note that this change assumes that the `ManagedObject` class is parameterized with a type argument of `ManagedObject`. If that's not the case, then the type argument may need to be adjusted accordingly.