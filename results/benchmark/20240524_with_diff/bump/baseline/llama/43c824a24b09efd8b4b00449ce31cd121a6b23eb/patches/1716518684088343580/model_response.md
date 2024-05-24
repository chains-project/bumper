```java
private static List<String> extractList(DataElement cache, JsonPathCache jsonPathCache, String jsonPath) {
    List<XmlFieldInstance> instances = jsonPathCache.get(jsonPath);
    List<String> values = new ArrayList<>();
    if (instances != null)
      for (XmlFieldInstance instance : instances)
        values.add(instance.getValue());
    return values;
}
```