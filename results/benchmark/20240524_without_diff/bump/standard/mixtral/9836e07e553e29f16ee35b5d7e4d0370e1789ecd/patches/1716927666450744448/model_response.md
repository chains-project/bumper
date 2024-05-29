Here's a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString())).getMessage(), new org.hamcrest.core.StringStartsWith("Unexpected query"));
}
```
The failure is caused by the `StringContains` matcher, which expects a single argument (a string), but is being passed two arguments (a boolean and a string). To fix the failure, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only expects a single argument. This way, the code will no longer throw a `java.lang.IllegalArgumentException`.