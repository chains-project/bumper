```java
private void registerHard(final MOGroup group) {
    final SortedMap<MOScope, ManagedObject> reg = server.getRegistry();
    DefaultMOContextScope contextScope = new DefaultMOContextScope(new OctetString(""), group.getScope());
    reg.put(contextScope, group);
}
```