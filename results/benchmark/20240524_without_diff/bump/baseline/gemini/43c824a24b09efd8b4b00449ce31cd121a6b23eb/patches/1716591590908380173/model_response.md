```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<XmlFieldInstance> instances = cache.get(branch.getJsonPath());
    List<String> values = new ArrayList<>();
    if (instances != null) {
        for (XmlFieldInstance instance : instances) {
            String value = instance.getValue();
            if (value != null) {
                values.add(value);
            }
        }
    }
    return values;
}
```