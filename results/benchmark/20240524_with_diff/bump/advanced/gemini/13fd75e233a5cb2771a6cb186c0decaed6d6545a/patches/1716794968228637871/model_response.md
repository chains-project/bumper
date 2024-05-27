```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    boolean isUploadStarted = false;
    String location = "";
    String range = "";
    String contentLength = "";
    String dockerUploadUuid = "";
    
    if (response.status().equals(com.artipie.http.rs.RsStatus.ACCEPTED)) {
        isUploadStarted = true;
        location = response.header("Location").get();
        range = response.header("Range").get();
        contentLength = response.header("Content-Length").get();
        dockerUploadUuid = response.header("Docker-Upload-UUID").get();
    }
    
    return new com.artipie.http.hm.ResponseMatcher(
        isUploadStarted,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith(false, location)),
        new com.artipie.http.hm.IsHeader("Range", range),
        new com.artipie.http.hm.IsHeader("Content-Length", contentLength),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString()))
    );
}
```