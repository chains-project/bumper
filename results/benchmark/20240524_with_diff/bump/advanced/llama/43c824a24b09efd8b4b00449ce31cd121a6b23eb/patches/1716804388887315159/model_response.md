```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.schema.MarcJsonSchema schema) {
    de.gwdg.metadataqa.api.json.DataElement element = schema.getPathByLabel("some_label"); // replace "some_label" with the actual label
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, element);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```