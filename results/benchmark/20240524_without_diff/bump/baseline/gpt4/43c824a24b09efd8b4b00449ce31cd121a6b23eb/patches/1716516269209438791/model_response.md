```java
  private static String extractFirst(JsonPathCache cache, DataElement element) {
    List<String> list = extractList(cache, element);
    if (!list.isEmpty())
      return list.get(0);
    return null;
  }
```