```java
private static List<String> extractList(JsonPathCache cache, de.gwdg.metadataqa.api.schema.MarcJsonSchema schema) {
    List<XmlFieldInstance> instances = cache.get(schema.getRecordId());
    List<String> values = new ArrayList<>();
    if (instances != null)
      for (XmlFieldInstance instance : instances)
        values.add(instance.getValue());
    return values;
}
```