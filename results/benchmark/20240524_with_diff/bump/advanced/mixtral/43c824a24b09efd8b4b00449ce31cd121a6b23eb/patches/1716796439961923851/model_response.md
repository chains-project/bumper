Here's the patched version of the `extractFirst` method that uses the new fully qualified name of the `JsonBranch` class:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

The change is in the second argument of the method, which now uses the fully qualified name of the `JsonBranch` class from the new library version.