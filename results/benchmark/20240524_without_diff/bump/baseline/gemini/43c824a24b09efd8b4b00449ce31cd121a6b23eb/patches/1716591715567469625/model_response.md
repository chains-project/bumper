```java
  private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = extractList(cache, branch);
    if (list != null && !list.isEmpty()) { // Check if list is not null before accessing its elements
      return list.get(0);
    }
    return null;
  }
```