```java
import com.artipie.http.auth.AuthUser;

...

        new com.artipie.docker.http.AuthScopeSlice(new com.artipie.docker.http.ScopeSlice() {
            @java.lang.Override
            public com.artipie.docker.http.Scope scope(final java.lang.String rqline) {
                cline.set(rqline);
                return new com.artipie.docker.http.Scope.FromString(action);
            }

            @java.lang.Override
            public com.artipie.http.Response response(final java.lang.String line, final java.lang.Iterable<java.util.Map.Entry<java.lang.String, java.lang.String>> headers, final org.reactivestreams.Publisher<java.nio.ByteBuffer> body) {
                return com.artipie.http.rs.StandardRs.OK;
            }
        }, ( headers, rline) -> java.util.concurrent.CompletableFuture.completedFuture(new com.artipie.http.auth.AuthScheme.Result() {
            @java.lang.Override
            public Optional<com.artipie.http.auth.Authentication.User> user() {
                return java.util.Optional.of(new AuthUser("alice", ""));
            }

            @java.lang.Override
            public java.lang.String challenge() {
                return "";
            }
        }), ( user, act) -> {
            caction.set(act);
            return true;
        }).response(line, com.artipie.http.Headers.EMPTY, com.artipie.asto.Content.EMPTY).send(( status, headers, body) -> java.util.concurrent.CompletableFuture.allOf()).toCompletableFuture().join();
...
```