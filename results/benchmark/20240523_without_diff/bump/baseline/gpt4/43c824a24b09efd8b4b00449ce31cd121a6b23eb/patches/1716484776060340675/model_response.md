```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = cache.getList(branch);
    if (list != null && !list.isEmpty())
      return list.get(0);
    return null;
}
```