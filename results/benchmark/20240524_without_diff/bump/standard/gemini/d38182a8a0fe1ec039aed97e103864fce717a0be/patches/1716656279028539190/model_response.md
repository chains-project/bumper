```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    if ("auth".equals(action)) {
        return new com.artipie.http.async.AsyncSlice(
            com.artipie.http.async.CompletableFutureSlice.wrap(
                new com.artipie.docker.http.auth.Auth().authorize(
                    new com.artipie.docker.http.auth.Auth.User(
                        "user",
                        "password"
                    )
                )
            )
        );
    } else if ("token".equals(action)) {
        return new com.artipie.http.async.AsyncSlice(
            com.artipie.http.async.CompletableFutureSlice.wrap(
                new com.artipie.docker.http.auth.Auth().token(
                    new com.artipie.docker.http.auth.Auth.User(
                        "user",
                        "password"
                    )
                )
            )
        );
    } else {
        return new com.artipie.http.Slice() {
            @java.lang.Override
            public java.util.concurrent.CompletionStage<com.artipie.http.Response> respond(
                final com.artipie.http.Request request
            ) {
                return java.util.concurrent.CompletableFuture.completedFuture(
                    new com.artipie.http.Response(
                        com.artipie.http.Status.BAD_REQUEST,
                        new com.artipie.http.Headers.From(
                            new java.util.LinkedHashMap<>()
                        ),
                        com.artipie.http.EMPTY_BODY
                    )
                );
            }
        };
    }
}
```