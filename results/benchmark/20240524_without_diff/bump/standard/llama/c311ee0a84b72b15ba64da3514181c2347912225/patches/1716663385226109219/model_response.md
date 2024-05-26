```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED, 
            new com.artipie.http.hm.IsHeader("Location", org.hamcrest.CoreMatchers.startsWith("/v2/test/blobs/uploads/")), 
            new com.artipie.http.hm.IsHeader("Range", "0-0"), 
            new com.artipie.http.hm.IsHeader("Content-Length", "0"), 
            new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.isEmptyString())));
}
```