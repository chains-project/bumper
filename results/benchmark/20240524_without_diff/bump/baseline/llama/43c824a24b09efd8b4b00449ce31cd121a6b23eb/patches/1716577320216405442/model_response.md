```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = extractList(cache, branch);
    return list.isEmpty() ? null : list.get(0);
}
```