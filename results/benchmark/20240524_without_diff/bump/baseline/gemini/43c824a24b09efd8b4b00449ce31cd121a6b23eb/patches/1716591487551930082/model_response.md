```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<String> values = new ArrayList<>();
    if (branch.getJsonPath() != null) {
        List<XmlFieldInstance> instances = cache.get(branch.getJsonPath());
        if (instances != null)
            for (XmlFieldInstance instance : instances)
                values.add(instance.getValue());
    }
    return values;
}
```