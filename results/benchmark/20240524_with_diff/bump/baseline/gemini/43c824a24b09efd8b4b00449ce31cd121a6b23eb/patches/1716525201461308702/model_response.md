```java
  private static List<String> extractList(JsonPathCache cache, JsonBranch branch) {
    DataElement element = cache.get(branch.getJsonPath());
    List<String> values = new ArrayList<>();
    if (element != null) {
      for (Object value : element.getValues()) {
        values.add(value.toString());
      }
    }
    return values;
  }
```