Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString())).getMessage(), new org.hamcrest.core.StringStartsWith("Unexpected query"));
}
```
In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only takes a single argument. This should resolve the error message you were seeing.