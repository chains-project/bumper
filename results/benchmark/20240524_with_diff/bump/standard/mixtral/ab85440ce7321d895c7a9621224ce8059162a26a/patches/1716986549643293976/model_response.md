Here is a patch that you can apply to the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing").toString())).getMessage(), new org.hamcrest.core.IsEqualIgnoringCase(new org.hamcrest.core.StringStartsWith("Unexpected query")));
}
```
The failure was caused by the fact that the constructor for `StringContains` no longer accepts a `boolean` argument in the new version of the library. To fix the error, I have replaced the `StringContains` matcher with an `IsEqualIgnoringCase` matcher that checks if the string starts with the substring "Unexpected query". This should have the same effect as the original code, but it will not cause a compilation error with the new version of the library.