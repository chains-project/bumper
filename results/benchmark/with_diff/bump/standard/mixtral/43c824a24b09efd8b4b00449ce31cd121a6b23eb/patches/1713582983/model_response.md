Here's a patch that you can apply to the failing client code:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.marc.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

In this patch, I changed the type of the `branch` parameter from `JsonBranch` to `de.gwdg.metadataqa.marc.JsonBranch` to match the new fully qualified name of the `JsonBranch` class in the updated library version.