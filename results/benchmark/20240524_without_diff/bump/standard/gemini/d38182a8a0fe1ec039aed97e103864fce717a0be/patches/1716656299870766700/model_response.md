```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.http.async.AsyncSlice(
        new com.artipie.http.async.CompletableFutureSlice(
            com.artipie.asto.test.TestResource.resourceFromClasspath("com/artipie/docker/auth/token.json")
                .thenApply(
                    content -> new com.artipie.http.Response(
                        com.artipie.http.Status.OK,
                        com.artipie.http.Headers.EMPTY,
                        com.artipie.http.async.AsyncResponse.CRLF,
                        com.artipie.http.async.AsyncResponse.EMPTY
                    )
                )
        )
    );
}
```