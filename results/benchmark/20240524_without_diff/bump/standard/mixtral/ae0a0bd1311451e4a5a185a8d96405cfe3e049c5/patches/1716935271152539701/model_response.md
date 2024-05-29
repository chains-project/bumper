Here's a fixed version of the code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString())).getMessage(), new org.hamcrest.core.StringStartsWith("Unexpected query"));
}
```
The change is in the `StringContains` matcher, which was replaced with `StringStartsWith` to match the expected argument list.