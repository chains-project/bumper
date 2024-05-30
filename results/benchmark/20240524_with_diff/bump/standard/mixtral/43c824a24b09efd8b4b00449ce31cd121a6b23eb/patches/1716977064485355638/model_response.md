Here's the fixed version of the `extractFirst` method that uses the new class `DataElement` instead of `JsonBranch`:

```java
private static String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
    List<String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

In the new library version, the class `JsonBranch` has been removed and replaced with `DataElement`. Therefore, we need to update the method signature to use `DataElement` instead. The rest of the method remains unchanged.