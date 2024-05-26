Here'Qs the updated `extractFirst` method with the necessary changes to use the new version of the library:

```java
private static String extractFirst(PathCache cache, DataElement branch) {
    List<String> list = MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

In the updated code, I replaced `de.gwdg.metadataqa.api.model.pathcache.JsonPathCache` with `de.gwdg.metadataqa.api.model.pathcache.PathCache` and `de.gwdg.metadataqa.api.json.JsonBranch` with `de.gwdg.metadataqa.api.json.DataElement`.