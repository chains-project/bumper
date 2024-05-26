```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    java.lang.String message = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(com.artipie.http.rq.RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString()).digest()).getMessage();
    org.hamcrest.MatcherAssert.assertThat(message, org.hamcrest.CoreMatchers.containsString("Unexpected query"));
}
```