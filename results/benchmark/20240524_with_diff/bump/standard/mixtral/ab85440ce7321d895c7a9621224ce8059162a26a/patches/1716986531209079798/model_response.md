Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    boolean contains = false;
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString()).digest()).getMessage(), new org.hamcrest.core.StringContains(contains, "Unexpected query"));
}
```

The patch creates a new variable `contains` and initializes it to `false`. It then uses this variable as the first argument to the `StringContains` constructor. This fixes the error message by providing a single argument to the constructor, which is required by the updated library version.