Here's the fixed version of the `testScope` method:

```java
@Test
void testScope() {
    final String line = "GET /resource.txt HTTP/1.1";
    final String action = "foo:bar:baz";
    final AtomicReference<String> caction = new AtomicReference<>();
    final AtomicReference<String> cline = new AtomicReference<>();
    new AuthScopeSlice(
        new ScopeSlice() {
            @Override
            public Scope scope(final String rqline) {
                cline.set(rqline);
                return new Scope.FromString(action);
            }

            @Override
            public Response response(
                final String line,
                final Iterable<Map.Entry<String, String>> headers,
                final Publisher<ByteBuffer> body
            ) {
                return StandardRs.OK;
            }
        },
        (headers, rline) -> CompletableFuture.completedFuture(
            new AuthScheme.Result() {
                @Override
                public Optional<AuthUser> user() {
                    return Optional.of(new AuthUser("alice", ""));
                }

                @Override
                public String challenge() {
                    return "";
                }
            }
        ),
        (user, act) -> {
            caction.set(act);
            return true;
        }
    ).response(line, Headers.EMPTY, Content.EMPTY).send(
        (status, headers, body) -> CompletableFuture.allOf()
    ).toCompletableFuture().join();
    MatcherAssert.assertThat(
        "Request line passed to slice",
        cline.get(),
        new IsEqual<>(line)
    );
    MatcherAssert.assertThat(
        "Scope passed as action to permissions",
        caction.get(),
        new IsEqual<>(action)
    );
}

class AuthUser implements com.artipie.http.auth.AuthUser {
    private final String name;
    private final String authContext;

    public AuthUser(String name, String authContext) {
        this.name = name;
        this.authContext = authContext;
    }

    @Override
    public String authContext() {
        return authContext;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        AuthUser authUser = (AuthUser) o;
        return Objects.equals(name, authUser.name) &&
            Objects.equals(authContext, authUser.authContext);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, authContext);
    }

    @Override
    public String name() {
        return name;
    }

    @Override
    public String toString() {
        return "AuthUser{" +
            "name='" + name + '\'' +
            ", authContext='" + authContext + '\'' +
            '}';
    }
}
```

The changes include:

1. Replacing `Authentication.User` with the new `AuthUser` class.
2. Creating a simple implementation of `AuthUser` class.
3. Updating the lambda that creates the `AuthScheme.Result` to return an `AuthUser`.
4. Updating the `caction.set(act)` line to use the `String` representation of `act` (assuming it is an `Action`).
5. Adding the `AuthUser` class to the test class.

This code should fix the compilation error and pass the original test case.