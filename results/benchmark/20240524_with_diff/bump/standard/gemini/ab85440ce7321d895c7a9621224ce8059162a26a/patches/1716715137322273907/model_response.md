```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString()).digest()).getMessage(), new org.hamcrest.core.StringContains(false, "Unexpected query", ""));
}
```