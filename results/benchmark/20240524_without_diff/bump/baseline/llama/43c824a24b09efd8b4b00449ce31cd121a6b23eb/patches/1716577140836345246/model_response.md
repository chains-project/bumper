```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    Object instances = cache.get(branch.getJsonPath());
    List<String> values = new ArrayList<>();
    if (instances instanceof List) {
        for (Object instance : (List) instances) {
            if (instance instanceof XmlFieldInstance) {
                values.add(((XmlFieldInstance) instance).getValue());
            }
        }
    }
    return values;
}
```