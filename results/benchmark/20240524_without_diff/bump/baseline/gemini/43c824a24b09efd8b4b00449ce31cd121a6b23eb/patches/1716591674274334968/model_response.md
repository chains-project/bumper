```java
  private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = extractList(cache, branch);
    if (list.isEmpty()) {
      return null;
    } else {
      return list.get(0);
    }
  }
```