```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    if ("auth".equals(action)) {
        return new com.artipie.http.async.AsyncSlice(
            new com.artipie.http.async.CompletableFutureSlice(
                java.util.concurrent.CompletableFuture.completedFuture(
                    new com.artipie.http.Response(
                        java.net.HttpURLConnection.HTTP_OK,
                        new com.artipie.http.headers.Text("text/plain", "OK")
                    )
                )
            )
        );
    } else {
        return new com.artipie.http.async.AsyncSlice(
            new com.artipie.http.async.CompletableFutureSlice(
                java.util.concurrent.CompletableFuture.completedFuture(
                    new com.artipie.http.Response(
                        java.net.HttpURLConnection.HTTP_BAD_REQUEST,
                        new com.artipie.http.headers.Text("text/plain", "Bad action")
                    )
                )
            )
        );
    }
}
```