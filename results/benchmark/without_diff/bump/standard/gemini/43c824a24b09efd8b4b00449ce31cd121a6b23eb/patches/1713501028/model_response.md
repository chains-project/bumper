```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch.toPath());
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```