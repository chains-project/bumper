```java
private static String extractFirst(DataElement cache, JsonBranch branch) {
    List<String> list = extractList(cache, branch);
    if (!list.isEmpty())
      return list.get(0);
    return null;
}
```