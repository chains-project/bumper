Here is a proposed patch for the failing client code:
```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, Object branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, (jsonbranch) -> jsonbranch.getBranch());
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```
Note that I changed the type of the `branch` parameter from `JsonBranch` to `Object`, and added a lambda expression to the `extractList` method call that converts the `branch` object to a `JsonBranch` object. This assumes that the `MarcFactory.extractList` method has been updated to accept a function that converts an arbitrary object to a `JsonBranch` object. If this is not the case, then further modifications may be necessary.