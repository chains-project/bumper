```java
// TODO: review this AI generated patch!
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.model.JsonBranch branch) {
    java.util.List<java.lang.String> list = extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```