```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    String uploadUUID = "upload-" + UUID.randomUUID().toString();
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith(false, "/v2/test/blobs/uploads/" + uploadUUID)), new com.artipie.http.hm.IsHeader("Range", "0-0"), new com.artipie.http.hm.IsHeader("Content-Length", "0"), new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())));
}
```