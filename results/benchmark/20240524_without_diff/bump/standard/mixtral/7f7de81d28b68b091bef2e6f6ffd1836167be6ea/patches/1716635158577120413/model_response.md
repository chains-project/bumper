Here'v a possible patch for the `registerHard` method. The issue is caused by the fact that the `SortedMap` type is not compatible between different versions of the library.

To fix this, you can create a new `SortedMap` instance with the same key and value types as the one returned by `server.getRegistry()`, then put the new element into this new instance and set it back to the `server` object.

Here's the modified code:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        final SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        SortedMap<MOScope, ManagedObject<?>> newReg = new TreeMap<>(reg);
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        newReg.put(contextScope, group);
        registry.set(server, newReg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
  }
}
```

This code creates a new `TreeMap` instance with the same generic types as the original `SortedMap`, then puts the new element into this new instance and sets it back to the `server` object. This should avoid the type compatibility issue.