```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<Object> instances = cache.get(branch.getJsonPath());
    List<String> values = new ArrayList<>();
    if (instances != null)
        for (Object instance : instances)
            if (instance instanceof XmlFieldInstance)
                values.add(((XmlFieldInstance) instance).getValue());
    return values;
}
```