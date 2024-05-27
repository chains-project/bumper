Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getMessage(), new org.hamcrest.core.StringStartsWith("Unexpected path"));
}
```
In the original code, the `StringContains` matcher was used incorrectly with a boolean argument. The `StringStartsWith` matcher has been used instead to check if the string starts with the expected substring.