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
            registry.set(server, (SortedMap<MOScope, ManagedObject>) reg);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            log.warn("could not set server registry", e);
        }
    }
```
In your code, the `registry` field is of type `SortedMap<MOScope, ManagedObject>`, but you're trying to assign it a value of type `SortedMap<MOScope, ManagedObject<?>>`. The `?` wildcard character in the type parameter of `ManagedObject<?>` is not compatible with the type parameter of `ManagedObject` in the `registry` field.


To fix this issue, you can cast the `reg` variable to `SortedMap<MOScope, ManagedObject>` before assigning it to the `registry` field. This tells the compiler that you know the type of the `reg` variable is different from the type of the `registry` field, but you still want to assign it to the field.

Alternatively, you could change the type of the `registry` field to `SortedMap<MOScope, ManagedObject<?>>` to match the type of the `reg` variable, but this might require further changes to your code to ensure compatibility with the rest of the program.