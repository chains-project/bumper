Here's the patch that you can apply to fix the error:
```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")), new com.artipie.http.hm.IsHeader("Range", "0-0"), new com.artipie.http.hm.IsHeader("Content-Length", "0"), new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsInstanceOf(String.class))));
}
```
In this patch, I replaced the `org.hamcrest.core.StringStartsWith` matcher with `org.hamcrest.core.IsInstanceOf` matcher for the `Docker-Upload-UUID` header's value. This way, we avoid passing the `boolean` argument to the `StringStartsWith` constructor, which was causing the compilation error.