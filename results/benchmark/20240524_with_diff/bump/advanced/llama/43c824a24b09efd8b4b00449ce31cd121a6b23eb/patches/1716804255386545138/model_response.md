```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, java.lang.String branch) {
    de.gwdg.metadataqa.api.schema.MarcJsonSchema schema = new de.gwdg.metadataqa.api.schema.MarcJsonSchema();
    de.gwdg.metadataqa.api.json.DataElement dataElement = schema.getPathByLabel(branch);
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(dataElement);
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```