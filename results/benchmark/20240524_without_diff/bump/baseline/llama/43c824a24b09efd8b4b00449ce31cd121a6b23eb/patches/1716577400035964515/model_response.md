```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    Object result = JsonPath.read(branch, cache.getPath());
    if (result instanceof List) {
        List<?> list = (List<?>) result;
        if (!list.isEmpty())
            return list.get(0).toString();
    }
    return null;
}
```