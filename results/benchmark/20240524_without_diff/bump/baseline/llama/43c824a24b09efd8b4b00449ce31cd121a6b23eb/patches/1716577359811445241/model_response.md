```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    Object result = cache.read(branch);
    if (result instanceof List) {
        List<?> list = (List<?>) result;
        if (!list.isEmpty())
            return list.get(0).toString();
    }
    return null;
}
```