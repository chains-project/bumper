```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.schema.MarcJsonSchema schema) {
    de.gwdg.metadataqa.api.json.DataElement element = schema.getPathByLabel("default");
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, element);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```