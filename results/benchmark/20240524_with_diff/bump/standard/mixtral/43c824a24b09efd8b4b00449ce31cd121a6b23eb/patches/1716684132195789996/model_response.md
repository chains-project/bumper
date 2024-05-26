Here's the patched version of the `extractFirst` method that uses the new `DataElement` class instead of `JsonBranch`:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

This patch assumes that the `extractList` method of `MarcFactory` has been updated to accept a `DataElement` instead of `JsonBranch`. If that's not the case, further modifications might be required.