```java
private static List<String> extractList(DataElement cache, JsonPathCache pathCache) {
    List<XmlFieldInstance> instances = pathCache.get(cache.getJsonPath());
    List<String> values = new ArrayList<>();
    if (instances != null)
      for (XmlFieldInstance instance : instances)
        values.add(instance.getValue());
    return values;
}
```