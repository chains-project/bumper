Here is a patch that you can apply to the failing client code:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

The only change I made is to replace the type of the `branch` parameter from `JsonBranch` to `de.gwdg.metadataqa.api.json.JsonBranch`. This is based on the information provided in the error message and the list of changes in the new library version. The `JsonBranch` class has been removed, and has been replaced by `de.gwdg.metadataqa.api.json.JsonBranch`.