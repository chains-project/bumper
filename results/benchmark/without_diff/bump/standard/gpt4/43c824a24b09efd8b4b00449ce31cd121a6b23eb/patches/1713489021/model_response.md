```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, java.lang.Object branch) {
    java.util.List<java.lang.String> list = extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```