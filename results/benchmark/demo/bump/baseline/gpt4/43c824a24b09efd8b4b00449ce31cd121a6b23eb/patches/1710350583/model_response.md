```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<XmlFieldInstance> instances = cache.get(branch.getJsonBranchPath());
    List<String> values = new ArrayList<>();
    if (instances != null)
        for (XmlFieldInstance instance : instances)
            values.add(instance.getInstanceValue());
    return values;
}
```