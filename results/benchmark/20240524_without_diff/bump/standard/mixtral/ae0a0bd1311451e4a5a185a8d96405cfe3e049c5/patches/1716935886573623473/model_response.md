Here's a possible patch for the code:
```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    boolean ignoreCase = false;
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith(ignoreCase, "/v2/test/blobs/uploads/")), new com.artipie.http.hm.IsHeader("Range", "0-0"), new com.artipie.http.hm.IsHeader("Content-Length", "0"), new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())));
}
```
The patch creates a new variable `ignoreCase` and sets it to `false`. This variable is then passed as the first argument to the `StringStartsWith` constructor, replacing the unused `boolean` argument that was causing the compilation error.