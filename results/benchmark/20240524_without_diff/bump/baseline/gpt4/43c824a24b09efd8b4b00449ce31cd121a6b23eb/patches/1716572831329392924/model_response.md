```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<Object> list = cache.read(branch.getJsonPath());
    if (list != null && !list.isEmpty())
      return list.get(0).toString();
    return null;
}
```