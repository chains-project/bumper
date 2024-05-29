Here's the proposed patch:

```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).name(), new org.hamcrest.core.StringStartsWith("Unexpected path"));
}
```

In this patch, I replaced the `StringContains` matcher with `StringStartsWith` matcher, which only takes a single argument, as required by the constructor. This should fix the compilation error.