Here's the fixed code:

```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).name(), new org.hamcrest.core.StringContains("Unexpected path"));
}
```

The issue was caused by using the wrong version of `StringContains` constructor. Instead of using `StringContains(boolean negated, String substring)`, I changed it to `StringContains(String substring)`.