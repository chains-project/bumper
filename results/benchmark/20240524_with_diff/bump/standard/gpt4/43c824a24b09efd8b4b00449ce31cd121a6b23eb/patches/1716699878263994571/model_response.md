```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement dataElement) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, dataElement);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```