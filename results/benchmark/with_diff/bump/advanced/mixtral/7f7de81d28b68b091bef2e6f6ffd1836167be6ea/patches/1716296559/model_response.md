Here's a possible patch for the `registerHard` method that should fix the type mismatch error:

```java
private void registerHard(final MOGroup group) {
    try {
        final Field registry = server.getClass().getDeclaredField("registry");
        registry.setAccessible(true);
        @SuppressWarnings("unchecked")
        SortedMap<MOScope, ManagedObject<?>> reg = server.getRegistry();
        DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
        reg.put(contextScope, group);
        registry.set(server, reg);
    } catch (NoSuchFieldException | IllegalAccessException e) {
        log.warn("could not set server registry", e);
    }
}
```

The only change I made is to add a wildcard `?` to the type parameter of the `SortedMap` variable `reg`. This allows the compiler to infer the correct type argument based on the value returned by `server.getRegistry()`.

Note that the `@SuppressWarnings` annotation is used to suppress the "raw types" warning that results from using a raw type (`SortedMap`) instead of a parameterized type (`SortedMap<MOScope, ManagedObject<?>>`). This is necessary because the raw type is required to compile the code using the Java 7 compiler. However, if you're using a newer version of Java, you can remove the wildcard and use `SortedMap<MOScope, ManagedObject<>>` instead.