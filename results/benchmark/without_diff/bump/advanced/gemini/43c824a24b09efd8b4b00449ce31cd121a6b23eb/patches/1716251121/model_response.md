```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, org.everit.json.schema.ObjectSchema schema) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, schema);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```