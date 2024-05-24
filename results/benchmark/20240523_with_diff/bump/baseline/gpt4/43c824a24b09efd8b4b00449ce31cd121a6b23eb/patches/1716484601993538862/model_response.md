```java
  private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = cache.extractList(branch);
    if (!list.isEmpty())
      return list.get(0);
    return null;
  }
```