```java
private static List<String> extractList(JsonPathCache cache, DataElement branch) {
    List<XmlFieldInstance> instances = cache.get(branch);
    List<String> values = new ArrayList<>();
    if (instances != null)
      for (XmlFieldInstance instance : instances)
        values.add(instance.getValue());
    return values;
}
```