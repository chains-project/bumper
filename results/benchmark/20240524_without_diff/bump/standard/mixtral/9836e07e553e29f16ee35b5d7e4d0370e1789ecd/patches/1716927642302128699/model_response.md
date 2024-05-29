Here's the patched method with the error fixed:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    java.util.function.Predicate<String> pathPredicate = (path) -> !path.contains("Unexpected path");
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).name(), pathPredicate);
}
```
In this patch, I replaced the `StringContains` matcher with a custom predicate `pathPredicate` that checks if the path does not contain the substring "Unexpected path".