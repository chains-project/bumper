```java
private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    List<String> values = new ArrayList<>();
    try {
        List<XmlFieldInstance> instances = cache.get(branch.getJsonPath());
        if (instances != null)
            for (XmlFieldInstance instance : instances)
                values.add(instance.getValue());
    } catch (NoSuchElementException e) {
        System.out.println("Element not found: " + e.getMessage());
    }
    return values;
}
```