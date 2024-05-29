Here's the proposed patch:
```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    boolean ignoreCase = false;
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith(ignoreCase, "/v2/test/blobs/uploads/")), new com.artipie.http.hm.IsHeader("Range", "0-0"), new com.artipie.http.hm.IsHeader("Content-Length", "0"), new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())));
}
```
The issue is caused by the `StringStartsWith` constructor being called with two arguments, while it only accepts one. I've added a boolean variable `ignoreCase` to make the code compile again.