Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    boolean contains = false;
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString()).digest()).getMessage(), new org.hamcrest.core.StringContains(contains, "Unexpected query"));
}
```
The patch creates a new variable `contains` and initializes it to `false`. Then, it uses this variable as the first argument of the `StringContains` constructor, instead of the boolean literal `false`. This is because the `StringContains` constructor now requires two arguments, instead of one, due to the changes in the library version.