```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    List<String> list = new ArrayList<>();
    for (String value : cache.read(branch)) {
        list.add(value);
    }
    if (!list.isEmpty())
      return list.get(0);
    return null;
}
```