Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString())).getMessage(), new org.hamcrest.core.StringStartsWith("Unexpected query"));
}
```
The failure is caused by the fact that the constructor of `StringContains` no longer accepts a second boolean argument in the new library version. Instead, we can use the `StringStartsWith` matcher to check if the message starts with the expected string.