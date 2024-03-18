```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<XmlFieldInstance> instances = cache.get(branch.getPath());
    List<String> values = new ArrayList<>();
    if (instances != null)
      for (XmlFieldInstance instance : instances)
        values.add(instance.getValue());
    return values;
}
```