Here's the proposed patch to fix the error:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    boolean ignoreCase = false;
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith(ignoreCase, "/v2/test/blobs/uploads/")), new com.artipie.http.hm.IsHeader("Range", "0-0"), new com.artipie.http.hm.IsHeader("Content-Length", "0"), new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())));
}
```

The error message indicates that the constructor for `StringStartsWith` now requires only one argument, a `String`, instead of two. To fix this, I've added a new variable `ignoreCase` to replace the second argument, and set it to `false`. This should allow the code to compile with the new library version.