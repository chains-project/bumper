```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list;
    try {
        list = cache.extractList(branch);
    } catch (Exception e) {
        list = new ArrayList<>();
    }
    if (!list.isEmpty())
        return list.get(0);
    return null;
}
```