```java
private void registerHard(final MOGroup group) {
    final SortedMap<MOScope, ManagedObject> registry = server.getRegistry();
    final DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
    registry.put(contextScope, group);
}
```