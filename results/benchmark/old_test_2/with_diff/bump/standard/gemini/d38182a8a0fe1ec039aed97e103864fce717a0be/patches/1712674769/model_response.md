```java
import com.artipie.http.auth.AuthUser;

...

        java.util.concurrent.CompletableFuture.completedFuture(new com.artipie.http.auth.AuthScheme.Result() {
            @java.lang.Override
            public Optional<com.artipie.http.auth.Authentication.User> user() {
                return java.util.Optional.of(new com.artipie.http.auth.AuthUser("alice", ""));
            }

            @java.lang.Override
            public java.lang.String challenge() {
                return "";
            }
        }), ( user, act) -> {
            caction.set(act);
            return true;
        }).response(line, com.artipie.http.Headers.EMPTY, com.artipie.asto.Content.EMPTY).send(( status, headers, body) -> java.util.concurrent.CompletableFuture.allOf()).toCompletableFuture().join();
```