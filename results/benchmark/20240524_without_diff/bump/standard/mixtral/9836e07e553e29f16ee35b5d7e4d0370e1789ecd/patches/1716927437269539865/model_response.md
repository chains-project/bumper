Here's a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getName(), new org.hamcrest.core.StringStartsWith("Unexpected path"));
}
```
In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which takes a single argument. This should fix the error message you were seeing, which was caused by passing two arguments to the `StringContains` constructor instead of one.