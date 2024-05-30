Here's the proposed patch for the failing client code:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

In this patch, I replaced the `JsonBranch` class from the old package `de.gwdg.metadataqa.marc` with the new one from the package `de.gwdg.metadataqa.api.json`. This should resolve the "cannot find symbol" error related to the `JsonBranch` class.